# Go-Block Cipher
> A block cipher algorithm using Feistel Network


## Table of Contents
* [Introduction](#introduction)
* [Description](#description)
* [How to run](#how-to-run)


## Introduction
This project was created by:
| No. | Name | Student ID |
| :---: | :---: | :---: |
| 1. | Hansel Valentino Tanoto | 13520046 |
| 2. | Ghebyon Tohada Nainggolan | 13520079 |
| 3. | Afrizal Sebastian | 13520120 |


## Description
Go-Block Cipher is a simple block cipher algorithm using Feistel Network as the core algorithm. It is a symmetric block cipher algorithm that use 128-bit block size and 128-bit key size. Go-Block Cipher main algorithm consists of an initial permutation, 16 rounds of Feistel Network, and a final substitution. Its Feistel Network and Internal Key Generator are implemented using various substitution and transposition operations which ensure the security of the algorithm based on the principles of diffusion and confusion. Below is the strcuture of the main algorithm and Feitel Network.

<img src="./img/main_algo.jpg" width=48% height=350>
<img src="./img/feistel_network.jpg" width=48% height=350>


## How to run
1. Clone this repository and open its directory in the terminal console
2. Run the `main.py` program using command `python src/main.py` in the terminal console
3. Go-Block Cipher is ready to use
