# unpacker-parser

- For usage and 'auto-setup' I recommend to use docker, from dictionary where docker-compose.yml is located run command `docker-compose up --build`
othervise make standard procedure of making python venv, installing reqirements etc.

- For running script in container use command `docker ps` to get id of container, then use `docker exec -it <id> bash` to run bash in container, then you can do work it with like with classic linux.  

- To run tests make sure that you are located in /tests directory command `pytest`

- To run script_ukol.py run command `python script_ukol.py -d` I recomnend to run in in directory where the script is located. 

- I implemented little extra feature that also provide this script with ability to download example file from website so before you run any other feature just make sure you have that specific file downloaded. (If you downloaded xml file manualy, make sure you store it in `./xml/export_full.xml` from location where is your current working directory, otherwise the script will not find it)

- For next steps there are options of script which you can use to run it with: 
 `Run script with single param: python script.py -x x[-c (count products), -l (listing products), -ln (nested list), -it (nested list partialy) -d (download)]'`

 - parameter '-it' aka nested list partially is just small addition that whole output of products with their parts will not run out over your eyes but after every product program will wait for input (pressing any key) to print next one. 







