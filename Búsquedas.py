{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ingrese el intervalo de interés utilizando el formato yyyymmdd\n",
      "Inicio: 20180101\n",
      "Fin: 20180202\n",
      "Desea alguna hora u horas en particular?\n",
      "S/N: N\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import datetime\n",
    "import os\n",
    "import numpy as np\n",
    "\n",
    "print(\"Ingrese el intervalo de interés utilizando el formato yyyymmdd\")\n",
    "inicio = datetime.datetime.strptime(input(\"Inicio: \"), \"%Y%m%d\")    \n",
    "fin = datetime.datetime.strptime(input(\"Fin: \"), \"%Y%m%d\")\n",
    "while (fin-inicio).days > 185:\n",
    "    print(\"Actualmente solo soportamos busquedas menores a 184 días, por favor mofifique su busqueda.\")\n",
    "    inicio = datetime.datetime.strptime(input(\"Inicio: \"), \"%Y%m%d\")\n",
    "    fin = datetime.datetime.strptime(input(\"Fin: \"), \"%Y%m%d\")\n",
    "dias = []\n",
    "lista = []\n",
    "for i in range(((fin-inicio).days)+1):\n",
    "    dias.append((inicio + datetime.timedelta(days=i)).strftime('%Y%m%d'))\n",
    "print(\"Desea alguna hora u horas en particular?\")\n",
    "respuesta = input(\"S/N: \")\n",
    "while respuesta != 'S' and respuesta != 'N':\n",
    "    print(\"Por favor eliga Si o No\")\n",
    "    respuesta = input(\"S/N: \")\n",
    "if respuesta == 'S':\n",
    "    print(\"Ingrese la hora ó intervalo de horas en formato hhmm\")\n",
    "    horainicio = datetime.datetime.strptime(input(\"Inicio: \"), \"%H%M\")\n",
    "    horafin = datetime.datetime.strptime(input(\"Fin: \"), \"%H%M\")\n",
    "    horas = []\n",
    "    for h in range(len(dias)):\n",
    "        for j in range((horafin.hour-horainicio.hour)+1):\n",
    "            horas.append(dias[h] + (horainicio + datetime.timedelta(hours=j)).strftime('%H%M'))\n",
    "            for k in range(len(horas)):\n",
    "                dir_path = os.path.dirname(os.path.realpath(horas[k]))\n",
    "                for root, dirs, files in os.walk(dir_path):\n",
    "                    for file in files: \n",
    "                        if file.startswith(horas[k]):\n",
    "                            lista.append((root+'/'+str(file))[-16:])\n",
    "    lista = list(set(lista))\n",
    "    lista = list(np.sort(lista))\n",
    "\n",
    "elif respuesta == 'N':\n",
    "    for l in range(len(dias)):\n",
    "        dir_path = os.path.dirname(os.path.realpath(dias[l]))\n",
    "        for root, dirs, files in os.walk(dir_path):\n",
    "            for file in files: \n",
    "                if file.startswith(dias[l]):\n",
    "                    lista.append((root+'/'+str(file))[-16:])\n",
    "lista"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
