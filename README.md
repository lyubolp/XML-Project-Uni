# XML generator from DTD + wikipedia parser
This project includes a DTD parser and an XML generator which can use the parsed DTD to generate valid XML templates. In addition said XML templates can be automatically filled with content from Wikipedia using the Wikipedia API.

## How to setup
Make sure you have the following packages installed:
 - `pip3`
 - `virtualenv` (can be installed through `pip3` or your default package manager)

1. Set up virtual env `virtualenv -p python3 venv`
2. Activate virtual env `source venv/bin/activate`
3. Install the required packages `pip install -r requirements.txt`
4. Run the server `./run.sh`
5. Open your browser and go to http://127.0.0.1:5000/
6. Open a DTD file and optionally select a wiki article by name
7. Click the Generate button

## Examples
Generate DTD and parse info from wikipedia
1. Choose the file `data/sample-dtd/astronomicheski-obekt.dtd`
2. Enter wikipedia article title 'Астрономически обект'
3. Choose option 'Вземи заглавията на секциите и текста'
4. Click the Generate button
The output should be:
```xml
<article>
	<text>
		Астрономически обект...
	</text>
	<text>
		Примери за астрономически...
	</text>
	<title>
		Галактики редактиране | редактиране на кода
	</title>
	<text>
		Вселената може да се...
	</text>
</article>
```
