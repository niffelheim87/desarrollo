#!/bin/bash
resetOdoo(){
	sudo chmod -R 777 /home/omar/Desktop/desarrollo
	rm -rf /home/omar/Desktop/desarrollo/volumesOdoo/dataPostgreSQL
	rm -rf /home/omar/Desktop/desarrollo/volumesOdoo/odoo
	tar -xf dataPostgreSQL.tar
	tar -xf odoo.tar 
}
resetOdoo
