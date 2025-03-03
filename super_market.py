{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c465856c-1abe-4d78-8f9b-b2bf72026473",
   "metadata": {},
   "outputs": [],
   "source": [
    "products = {\"apple\":40, \"chips\":20, \"avacado\":115, \"cock\":40}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24423d70-de7e-42ff-965f-0502d097ab3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "_______________ Welcome To Wscubemart _______________\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your name:  harsh\n",
      "enter phone number:  987654\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "_______ products List _______\n",
      "        apple : 40\n",
      "        chips : 20\n",
      "        avacado : 115\n",
      "        cock : 40\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter product name you wish to buy:  apple\n",
      "enter quantity you wish to buy:  5\n",
      "do you wanna add more items?(yes/no)  no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "________________________________________\n",
      "name:  harsh\n",
      "phone:  987654\n",
      "apple price:  40 x 5.0 = 200.0\n",
      "________________________________________\n",
      "total amount:  200.0\n",
      "discount applied:  0 %\n",
      "________________________________________\n",
      "payable amount:  200.0\n",
      "________________________________________\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "next person?  harshita\n",
      "enter your name:  harshita\n",
      "enter phone number:  87654\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "_______ products List _______\n",
      "        apple : 40\n",
      "        chips : 20\n",
      "        avacado : 115\n",
      "        cock : 40\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter product name you wish to buy:  avacado\n",
      "enter quantity you wish to buy:  6\n",
      "do you wanna add more items?(yes/no)  no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "________________________________________\n",
      "name:  harshita\n",
      "phone:  87654\n",
      "avacado price:  115 x 6.0 = 690.0\n",
      "________________________________________\n",
      "total amount:  690.0\n",
      "discount applied:  5.0 %\n",
      "________________________________________\n",
      "payable amount:  655.5\n",
      "________________________________________\n"
     ]
    }
   ],
   "source": [
    "print(\"_\"*15,\"Welcome To Wscubemart\", \"_\"*15)\n",
    "while True:\n",
    "  cart = {}\n",
    "  amount = 0\n",
    "  name = input('enter your name: ')\n",
    "  phone_number = input('enter phone number: ')\n",
    "  discount = 0\n",
    "\n",
    "  print('_'*7, \"products List\", \"_\"*7)\n",
    "  for i,j in products.items():\n",
    "     print(' '*7,i, \":\",j)\n",
    "  while True:\n",
    "      p_name = input(\"enter product name you wish to buy: \")\n",
    "      quantity = float(input(\"enter quantity you wish to buy: \"))\n",
    "      value = []\n",
    "      value.append(products[p_name])\n",
    "      value.append(quantity)\n",
    "      value.append(quantity *products[p_name])\n",
    "      cart[p_name] = value\n",
    "      amount += products[p_name] * quantity\n",
    "      repeat = input(\"do you wanna add more items?(yes/no) \")\n",
    "      if repeat == \"no\":\n",
    "          break\n",
    "  if amount <=500: \n",
    "      discount = 0\n",
    "  elif amount <=1000:\n",
    "    discount = 0.05\n",
    "  elif amount <=3000:\n",
    "    discount = 0.10\n",
    "  else:\n",
    "    discount=0.15\n",
    "\n",
    "  act_amount = amount - (amount*discount)\n",
    "  print(\"_\"*40)\n",
    "  print(\"name: \", name)\n",
    "  print(\"phone: \",phone_number)\n",
    "  for i,j in cart.items():\n",
    "      print(i, \"price: \", j[0],\"x\",j[1],\"=\",j[2])\n",
    "\n",
    "  print(\"_\"*40)\n",
    "  print(\"total amount: \",amount)\n",
    "  print(\"discount applied: \", discount*100,\"%\")\n",
    "  print(\"_\"*40)\n",
    "  print(\"payable amount: \", act_amount)\n",
    "  print(\"_\"*40)\n",
    "  n_person = input(\"next person? \")\n",
    "  if n_person == \"no\":\n",
    "      break\n",
    "\n",
    "   \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9bab8055-d438-4e05-90d5-6f83bd4ffa92",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
