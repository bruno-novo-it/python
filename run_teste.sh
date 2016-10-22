#!/bin/bash


if [ -z "$1" ]
	then 
		echo "É necessário passar algum arquivo .py para funcionar ok?!"
		echo "Exemplo: ./run_teste.sh teste.py"
else
	python "$1"
fi

