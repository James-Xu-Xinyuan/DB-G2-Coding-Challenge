<h1>General Information</h1>

<h2>About</h2>

[Case Study: Description and Key Stakeholders](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314193853/Case+Study+Details)  
[User Requirements | Product Backlog](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314128449/User+Requirements)  
[Useful Terminology](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314128252/Q+As)  
[Suggested Approach](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1476493351/Suggested+Approach)  

<h2>Technologies and Algorithms</h2>

[Available Technologies](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314423043/Technology+Available+To+You)  
[Technical Details](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314128266/Technical+Details)  
[Deal Algorithm a.k.a. RandomDealData.py](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314423054/Deal+Algorithm)  
[Pricing Algorithm](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314128348/Pricing+Algorithm)  

<h1>Useful Concepts</h1>

<em>This section contains useful links if you need to review some basics.</em><br /> 

[Database Concepts](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1310785568/Database+Concepts+ABCs)  
[Docker Concepts](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1310785616/Docker+ABCs)  
[Flask Concepts](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1310589101/Flask+ABCs)  
[HTML Concepts](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314357422/HTML+Introduction)  
[JSON Concepts](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314193550/JSON+ABCs)  
[MySQL Concepts](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314128079/MySQL+ABCs)  
[TDD Concepts](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314193597/TDD+ABCs)  
[API, Web Services and Contracts Concepts](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314422972/API+Web+Services+and+Contracts)  



<h1>Cheat Sheets</h1>

<em>This section contains lists of short instructions for working with provided technologies.</em><br /> 

[Docker Cheat Sheet](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1310589098/Docker+Cheat+Sheet)  
[Flask Cheat Sheet](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314193504/Flask+Cheat+Sheet)  
[TDD Cheat Sheet](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314193604/TDD+Cheat+Sheet)  


<h1>HOW-TOs</h1>

<em>This section contains lists of detailed instructions with explanations for working with provided technologies.</em><br /> 

[Docker Container Deployment with Python HOW-TO](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314422910/Deploying+to+Docker+Container)  
[Docker ReactJS Apps Deployment HOW-TO](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314193587/Deploying+ReactJS+Applications+in+Docker)  
[SSE Stream in a ReactJS Apps HOW-TO](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314128122/Using+an+SSE+Stream+in+a+ReactJS+application)  
[AWS EC2 Python, Flask and SSE setup HOW-TO](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1313865922/AWS+EC2+Python+Flask+SSE+setup)  
[Database install and setup HOW-TO](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314193645/Database+install+and+setup)  
[Build Process HOW-TO](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314193613/Build+Process)  
[Python Flask HOW-TO](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1313865925/Hello+World+from+Python+Flask)  
[HTML5 SSE and Python HOW-TO incl. SSE, JS API, Python Generators, Data Stream Consume](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314128223/HTML5+SSE+and+Python)  
[SSE Stream into React UI HOW-TO](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1354596353/Example+SSE+Stream+into+React+UI)  
[Python Virtual Environments HOW-TO incl. Flask Installation](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1313865977/Python+Virtual+Environments)  
[Python Flask Application in a Docker Container HOW-TO](https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1314193692/Running+Python+Flask+Application+in+a+Docker+Container)  



<h1>Additional Information</h1>

<em>This section is intended for developers while working on a project.</em><br /> 

<h2>What to do if your lab crashed</h2>

<ol>
  <li>Open up Docker</li>
  <li>Click "Skip This Build"</li>
  <li>Open up Windows Power Shell</li>
  <li>Run <em>docker ps -a</em></li>
  <li>Run <em>docker run  -p 3306:3306 --name mysql-server -e MYSQL_ROOT_PASSWORD=ppp -d mysql:latest
</em></li>
  <li>Open up MySQL Workbench</li>
  <li>Select <em>+</em> creating <em>mysql-server</em> and enter the password <em>ppp</em></li>
  <li>Download Database Schema from <a href="https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1341718539/git+repos">Git Repos</li></a>
  <li>Run this SQL Script in MySQL Workbench</li>
  <li>Download Data generator and Webtier webservices from <a href="https://deliveringtechnology2018.atlassian.net/wiki/spaces/CS2020S/pages/1341718539/git+repos">Git Repos</li></a>
  <li>Open up PyCharm or Visual Studio Code</em></li>
  <li>Install the requirements for Data generator and Webtier webservices using <em>pip install -r requirements.txt</em></li>
  <li>Check the connection using your localhost, e.g. <em>127.0.0.1:8080/streamTest/sse</em></li>
</ol>

<h2>TBD if needed</h2>

