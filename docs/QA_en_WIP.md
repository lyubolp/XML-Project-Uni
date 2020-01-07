# XML Generator from DTD

## Authors

Ivan Luchev (https://github.com/luchev)

Lyuboslav Karev (https://github.com/lyubolp)

Faculty of mathematics and informatics Sofia University

Course: Software quality assurance

## Project description

The project is a web application which allows the user to input a valid DTD file and generate XML corresponding to that DTD, opening it in a web code editor for the user to continue editing.

Some specifically formatted DTDs have the option to be used as a template for a Wikipedia page. If the user has such a DTD, they can specify a Wiki page and what info they want to pull from that page. When generating the XML in this case it will also be filled with the information from the Wiki page.

## Introduction to the QA part of the project

The project is written in **python**. The testing is done using the python module **unittest**. In total there are **47 unit-tests**, which test all of the 9 modules in the project. The overall code coverage is **90%**, as 9/7 of the modules have 100% coverage. The remaining 2 files have untested methods, but they are not used anywhere in the project and exist only to complete the API the components, these methods belong to, provide. The testing done is **white-box testing**, because the project is very complex and there are a lot of staged of computation, which remain unknown to the end users. However all of these stages of the project have to work correctly so the user can use the final finished product effectively. Having so many hidden methods and overall computations in many hidden layers it would be incredibly hard to find bugs had we used black-box testing, because there are tens of methods being called between what the user sees as a GUI and the data being read and parsed. Hence we check the correctness of the program on each possible layer.

Test results: https://qa-xml-test-results.netlify.com/

## How were the tests written

The tests were written so they cover every possible path in the code execution, if we model the code as a graph from functions, methods, classes and if-else blocks. The tests start from the simplest and most basic methods like reading a file and checking its content and gradually build up to more complex methods, which rely on the simpler ones, such as generating a whole XML tree from parsed DTD objects. Most of these methods are protected/private and they are not usually accessible from outside the class/package they are in, however python allows us to break the encapsulation and have full access to protected/private methods and data fields. If we look at the program as a list of functionalities A -> B -> C -> ... (e.g read file -> check file content for errors -> parse content as DTD -> ...), first the functionality A is being tested, then B is tested (which relies on the correctness of A) and so on. Each possible middle point of the program execution is tested in order. To achieve this we have used the call-stack of the functionalities, to determine which function calls which. Here's an example of one such call-stack. On it we can see the functions at the bottom do not depend on anything else, so they are the first to be tested for correctness. Once we are certain they are covered and work properly we can start with the next set of functions (on the upper level in the graph), which depend on these basic functions, which we have already tested. This way going up the graph we check that each level works correctly before moving up to the next (more complex) one. This can be seen as doing a Width first traversal of the graph starting from the leaves and moving to the root.

![](https://imgur.com/NrSWhrN.png)

https://imgur.com/OCRNiWV

https://imgur.com/rjh86MX

https://imgur.com/NrSWhrN

## Осигуряване на пълно покритие на входните данни

За да се осигури, че не само сме тествали всички възможни методи в програмата, а и всички възможни входове сме разделили входа на класове на еквивалентност, които да покриват всички възможни входове. Тъй като програмата работи със файлове/стрингове, които трябва да представляват валидни DTD документи, най-общо разделянето на класове на еквивалентност може да е: несъществуващ файл, празен файл, файл с невалидни данни, файл с частично валидни данни, файл с напълно валидни данни. Това разделение важи и когато входа е string, а не файл. Отделно за тестването на функционалности може да разделим тези класове на еквивалентност на още повече класове. Например горните класове на еквивалентност са важни за нас, когато четен файл/стринг и трябва да вземем съдържанието. След като имаме съдържанието и сме проверили, че е валидно, попадаме в случая файл с напълно валидни данни. За да продължим тестването/изпълнението на програмата валидните данни могат да бъдат разделени в смисъла на DTD на 1 елемент, 1 елемент и 1 атрибут, множество елементи, множество елементи и множество атрибути и т.н.

## Осигуряване на пълно покритие на кода

За осигуряване, че максимална част от кода е тестван използвахме coverage.py, за да генерираме информация кои редове от кода са тествани и кои не.

Code coverage results: https://qa-xml-coverage.netlify.com/

## Заключение

Всички функционалности необходими на проекта да работи и всички функционалности, които проектът използва са тествани. Някой функционалности, които не се използват са оставени нетествани, но те съществуват, за да имат пълнота интерфейсите на софтуера. По този начин постигаме 100% покритие на проекта с тестове и 90% покритие на кода.

## Detailed test description

### dtd_parser

#### test_read_file_content

##### test_1element

| Description            | Test reading a DTD file with 1 DTD element       |                                                              |
| ---------------------- | ------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                             |                                                              |
| **Test step**          | **Description**                                  | **Expected result**                                          |
| 1                      | Create DTD parser object                         | A new DTD parser object is created                           |
| 2                      | Read file 1element.dtd                           | The file 1element.dtd is read into the object memory         |
| 3                      | Verify the content of the file is read correctly | The file content read from the file in the object is the same as the actual file |

##### test_2nested_elements

| Description            | Test reading a DTD file with 2 nested in each other DTD elements |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 2nested_elements.dtd                               | The file 2nested_elements.dtd is read into the object memory |
| 3                      | Verify the content of the file is read correctly             | The file content read from the file in the object is the same as the actual file |

##### test_1element_1attribute

| Description            | Test reading a DTD file with 1 element and 1 attribute |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read file 1element_1attribute.dtd                      | The file 1element_1attribute.dtd is read into the object memory |
| 3                      | Verify the content of the file is read correctly       | The file content read from the file in the object is the same as the actual file |

#### test_read_file_content_exceptions

##### test_non_dtd_tags

| Description            | Test reading a file which has invalid DTD tags               |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Verify that reading file invalid_token.dtd raises a Value Error | Reading the file invalid_token.dtd the DTD parser raises a Value Error |

##### test_invalid_element_children

| Description            | Test reading a DTD file which has invalid children elements  |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Verify that reading file invalid_element_children.dtd raises a Value Error | Reading the file invalid_element_children.dtd the DTD parser raises a Value Error |

#### test_tokenize_content_elements

##### test_1element

| Description            | Test generating DTD tokens from a file with 1 element |                                                      |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------- |
| **Initial conditions** | None                                                  |                                                      |
| **Test step**          | **Description**                                       | **Expected result**                                  |
| 1                      | Create DTD parser object                              | A new DTD parser object is created                   |
| 2                      | Read file 1element.dtd                                | The file 1element.dtd is read into the object memory |
| 3                      | Verify the parser has generated 1 DTD tokens          | The parser has generated 1 DTD tokens                |

##### test_2nested_elements

| Description            | Test generating DTD tokens from a file with 2 element |                                                              |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| **Initial conditions** | None                                                  |                                                              |
| **Test step**          | **Description**                                       | **Expected result**                                          |
| 1                      | Create DTD parser object                              | A new DTD parser object is created                           |
| 2                      | Read file 2nested_elements.dtd                        | The file 2nested_elements.dtd is read into the object memory |
| 3                      | Verify the parser has generated 2 DTD tokens          | The parser has generated 2 DTD tokens                        |

##### test_5nested_elements

| Description            | Test generating DTD tokens from a file with 5 element |                                                              |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| **Initial conditions** | None                                                  |                                                              |
| **Test step**          | **Description**                                       | **Expected result**                                          |
| 1                      | Create DTD parser object                              | A new DTD parser object is created                           |
| 2                      | Read file 5nested_elements.dtd                        | The file 5nested_elements.dtd is read into the object memory |
| 3                      | Verify the parser has generated 5 DTD tokens          | The parser has generated 5 DTD tokens                        |

##### test_12elements

| Description            | Test generating DTD tokens from a file with 12 element |                                                        |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                        |
| **Test step**          | **Description**                                        | **Expected result**                                    |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                     |
| 2                      | Read file 12elements.dtd                               | The file 12elements.dtd is read into the object memory |
| 3                      | Verify the parser has generated 12 DTD tokens          | The parser has generated 12 DTD tokens                 |

#### test_tokenize_content_attributes

##### test_1element_1attribute

| Description            | Test generating DTD tokens from a file with 1 element and 1 attribute |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 1element_1attribute.dtd                            | The file 1element_1attribute.dtd is read into the object memory |
| 3                      | Verify the parser has generated 2 DTD tokens                 | The parser has generated 2 DTD tokens                        |

##### test_1element_6attributes

| Description            | Test generating DTD tokens from a file with 1 element and 6 attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 1element_6attributes.dtd                           | The file 1element_6attributes.dtd is read into the object memory |
| 3                      | Verify the parser has generated 7 DTD tokens                 | The parser has generated 7 DTD tokens                        |

##### test_1element_2attributes

| Description            | Test generating DTD tokens from a file with 1 element and 2 attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 1element_2attributes.dtd                           | The file 1element_2attributes.dtd is read into the object memory |
| 3                      | Verify the parser has generated 3 DTD tokens                 | The parser has generated 3 DTD tokens                        |

##### test_9elements_3attributes

| Description            | Test generating DTD tokens from a file with 9 elements and 3 attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 9elements_3attributes.dtd                          | The file 9elements_3attributes.dtd is read into the object memory |
| 3                      | Verify the parser has generated 12 DTD tokens                | The parser has generated 12 DTD tokens                       |

##### test_11elements_6attributes

| Description            | Test generating DTD tokens from a file with 11 elements and 6 attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 11elements_6attributes.dtd                         | The file 11elements_6attributes.dtd is read into the object memory |
| 3                      | Verify the parser has generated 17 DTD tokens                | The parser has generated 17 DTD tokens                       |

#### test_tokenize_content_exceptions

##### test_empty_file

| Description            | Test raising exception from generating DTD tokens from an empty file |                                                        |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                        |
| **Test step**          | **Description**                                              | **Expected result**                                    |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                     |
| 2                      | Read file empty_file.dtd                                     | The file empty_file.dtd is read into the object memory |
| 3                      | Verify the parser has generated 0 DTD tokens                 | The parser has generated 0 DTD tokens                  |
| 4                      | Verify the parser has read no content from the file          | The parser has read an empty string as file content    |

##### test_dtd_mixed_with_text

| Description            | Test raising exception from generating DTD tokens from an empty file |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file dtd_mixed_with_text.dtd                            | The file dtd_mixed_with_text.dtd is read into the object memory |
| 3                      | Verify the parser has generated 0 DTD tokens                 | The parser has generated 0 DTD tokens                        |

#### test_parse_tokens_elements

##### test_1element

| Description            | Test parsing the DTD tokens to DTD objects from a file with 1 DTD element |                                                            |
| ---------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| **Initial conditions** | None                                                         |                                                            |
| **Test step**          | **Description**                                              | **Expected result**                                        |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                         |
| 2                      | Read file 1element.dtd                                       | The file 1element.dtd is read into the object memory       |
| 3                      | Verify the element note has 1 sub-element                    | The element note has 1 sub-element                         |
| 4                      | Verify the element note has empty element-name               | The element note has empty string for an element-name      |
| 5                      | Verify the element note's first child has name #PCDATA       | The element note's first child element is #PCDATA          |
| 6                      | Verify the element note's first child has no sub-elements    | The element note's first child element has no sub-elements |

##### test_1comment_1element

| Description            | Test parsing the DTD tokens to DTD objects from a file with 1 DTD element and 1 comment |                                                             |
| ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| **Initial conditions** | None                                                         |                                                             |
| **Test step**          | **Description**                                              | **Expected result**                                         |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                          |
| 2                      | Read file 1element.dtd                                       | The file 1element.dtd is read into the object memory        |
| 3                      | Verify the parser has generated 1 element                    | The parser has parsed 1 element and has ignored the comment |