{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1aac99d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter an integer (n): 13\n",
      "Total number of digit 1 appearing in all numbers up to 13 is: 6\n"
     ]
    }
   ],
   "source": [
    "def countDigitOne(n):\n",
    "    count = 0\n",
    "    factor = 1\n",
    "\n",
    "    while factor <= n:\n",
    "        quotient = n // (factor * 10)\n",
    "        remainder = n % (factor * 10)\n",
    "        count += quotient * factor + min(max(remainder - factor + 1, 0), factor)\n",
    "\n",
    "        factor *= 10\n",
    "\n",
    "    return count\n",
    "\n",
    "user_input = int(input(\"Enter an integer (n): \"))\n",
    "\n",
    "\n",
    "result = countDigitOne(user_input)\n",
    "print(\"Total number of digit 1 appearing in all numbers up to\", user_input, \"is:\", result)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2dbb26e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c3901bb",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
