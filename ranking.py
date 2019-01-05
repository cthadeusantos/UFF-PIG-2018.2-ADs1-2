#!/usr/bin/env python
# coding: UTF-8
#
## @package Ranking Class
#
#  @brief This class generate a ranking from inputs
#  @note calculate footrule and kemeny distance
#  @author Carlos Thadeu Santos - ID: 17113050228
#  @date 31-Aug-2018
#  @version 0.0.2 alpha
#
# Changelog
# v0.0.2 
# add "Rank is None" in initializeFromTuple
# add "Scores is None" in initializeFromList

from random import randint
from merge_sort import *
from binary_search import *

class Ranking:
    def __init__(self, arg):
        self.ranking = []
        self._inversoes = 0
        if type(arg) == list:
            self.initializeFromList(arg)
        elif type(arg) == tuple:
            self.initializeFromTuple(arg)
        elif type(arg) == int:
            self.initializeFromInt(arg)

    def initializeFromInt(self, n):
        #    @note Build a random rank between 1 and N.
        #    @param[in] n a integer number, must be 1 or greater
        #    @return a list
        #    @retval list
        #    @raises: ValueError
        try:
            if n < 1:
                raise ValueError('Inteiro deve estar entre 1 e n.')
        except ValueError:
            #raise Exception('Inteiro deve estar entre 1 e n.')
            print('Inteiro deve estar entre 1 e n.')
        else:
            self.ranking = self.__Shuffle(n)
            self._inversoes = self.setComputa_inversoes
            return self.ranking

    def initializeFromTuple(self, rank):
        """@note Build a rank from tuple.
           @param[in] rank a tuple
           @return a list
           @retval list
           @raises: ValueError, TypeError
           @example self.initializeFromTuple((0.34,.05,.6))
        """
        try:
            # Review after AD1 - 2018.09.12 - changelog for this method
            # add rank is None
            if not (len(rank)) or any(d is None for d in rank) or rank is None:
                raise TypeError("Ranking contém None ou valores duplicados")
                #raise Exception("Ranking contém None ou valores duplicados")
            if len(rank) != len(set(rank)):
                raise TypeError("Ranking contém None ou valores duplicados")
                #raise Exception("Ranking contém None ou valores duplicados")
        except TypeError:
            #raise TypeError("Ranking contém None ou valores duplicados")
            print ("Ranking contém None ou valores duplicados")
            #raise
#            raise Exception("Ranking contém None ou valores duplicados")
            #raise
        else:
            lista = list(rank)
            self.ranking = lista
            self._inversoes = self.setComputa_inversoes
            ranking = [0]*len(rank)
            count = 0
            ordenada = merge_sort(lista)  # n. log n
            # Faz pesquisa binária em tempo n. log n
            for x in lista: # loop n
                ranking[count] = len(rank) - binarySearch(ordenada, x) #+ 1  # pesquisa log n
                count += 1
            # resultado da busca binaria n . log n
            self.ranking = ranking
            return self.ranking

    def initializeFromList(self, scores):
        """@note Build a rank from scores.
           @param[in] scores a list
           @return a list
           @retval list
           @raises: ValueError, TypeError
           @example self.initializeFromList([0.34,.05,.6])
        """
        try:
            # Review after AD1 - 2018.09.12 - changelog for this method
            # add score is None
            if not (len(scores)) or any(d is None for d in scores) or scores is None:
                raise TypeError('Scores vazio ou contém elemento None ou valores duplicados!')
            if len(scores) != len(set(scores)):
                raise TypeError('Scores vazio ou contém elemento None ou valores duplicados!')
        except TypeError:
            #raise Exception('Scores vazio ou contém elemento None!')
            print('Scores vazio ou contém elemento None ou valores duplicados!')
        else:
            self.ranking = scores
            self._inversoes = self.setComputa_inversoes
            ranking = [0]*len(scores)
            count = 0
            ordenada = merge_sort(scores)  # n. log n
            # Faz pesquisa binária em tempo n. log n
            for x in scores: # loop n
                #ranking[count] = len(scores) - binarySearch(ordenada, x) # pesquisa log n
                ranking[count] = (len(scores)) - binarySearch(ordenada, x) # pesquisa feita em log n
                count += 1
            # resultado da busca binaria n . log n
            self.ranking = ranking
            return self.ranking

    @property
    def getNumItems(self):
        """@note Get itens number from ranking.
           @return a integer
           @retval integer
           @example self.getNumItems()
        """
        return len(self.ranking)

    #@property
    def getRank(self, i):
        """@note Return rank from item i.
           @param[in] i the item number
           @return a integer
           @retval integer
           @raises: ValueError
           @example self.getRank(1)
        """
        try:
            if i < 1 or i >= self.getNumItems:
                raise ValueError('Faixa de valor inválida!')
        except ValueError:
            #raise Exception('Faixa de valor inválida!')
            print('Faixa de valor inválida!')
        else:
            return self.ranking[i-1]

    def footrule(self, r1, r2):
        """@note Return footrule distance between two rankings.
           @param[in] r1 a list
           @param[in] r2 a list
           @return a integer
           @retval integer
           @raises: ValueError, TypeError
           @example object.footrule([1,2,3],[3,2,1])
        """
        footruleDistance = 0
        rank1 = r1.ranking
        rank2 = r2.ranking
        try:
            if not rank1 or not rank2:
                raise TypeError("Ranking não pode estar vazio ou ter tamanho diferente!")
            if len(rank1) != len(rank2):
                raise TypeError("Ranking não pode estar vazio ou ter tamanho diferente!")
        except TypeError:
            #raise Exception("Ranking não pode estar vazio ou ter tamanho diferente!")
            print("Ranking não pode estar vazio ou ter tamanho diferente!")
        #except ValueError:
        #    raise Exception("Rankings não podem ter tamanhos diferentes!")
        else:
            footruleDistance = 0
            for posicaoR1 in range(0, len(rank1), 1):
                footruleDistance = footruleDistance + abs(rank1[posicaoR1] - rank2[posicaoR1])
            return footruleDistance

    def kemeny(self, r1, r2):
        """@note Return footrule distance between two rankings.
           @param[in] r1 a list
           @param[in] r2 a list
           @return a integer
           @retval integer
           @raises: ValueError, TypeError
           @example object.kemeny([1,2,3],[3,2,1])
        """
        rank1 = r1.ranking
        rank2 = r2.ranking
        try:
            if not rank1 or not rank2:
                raise TypeError("Ranking não pode estar vazio ou ter tamanhos diferentes!")
            if len(rank1) != len(rank2):
                raise TypeError("Ranking não pode estar vazio ou ter tamanhos diferentes!")
        except TypeError:
            #raise Exception("Ranking não pode estar vazio ou ter tamanhos diferentes!")
            print("Ranking não pode estar vazio ou ter tamanhos diferentes!")
        #except ValueError:
        #    raise Exception("Rankings não podem ter tamanhos diferentes!")
        else:
            kemenyDistance = 0
            comprimento = len(rank1)
            # Executa bubble sort o(n)
            for i in range(len(rank1)):
                for j in range(i, len(rank1)):
                    if rank1[i] > rank1[j]:
                        rank1[i], rank1[j] = rank1[j], rank1[i]
                        rank2[i], rank2[j] = rank2[j], rank2[i]
            for i in range(0, comprimento):
                for j in range(i + 1,comprimento):
                    if (rank1[i] < rank1[j]) and (rank2[i] > rank2[j]):
                        kemenyDistance += 1
            return kemenyDistance

    def fDist(self, other):
        """@note Return footrule distance between two rankings.
           @param[in] other a list
           @return a integer
           @retval integer
           @example self.fDist([1,2,3])
        """
        return self.footrule(self, other)

    def kDist(self, other):
        """@note Return kemeny distance between two rankings.
           @param[in] other a list
           @return a integer
           @retval integer
           @example self.kDist([1,2,3])
        """
        return self.kemeny(self, other)

    def invCount(self):
        """@note Return a inversions number from ranking.
           @return a integer
           @retval integer
           @example self.invCount([1,2,3])
        """
        # Aqui funciona em o(1) conforme pedido na página 12
        # Na criação da instancia, calcula atraves de computa_inversoes o número de inversoes
        return self._inversoes

    # Minhas implementações - opcionais
    @property
    def setComputa_inversoes(self):
        """@note Auxyliary method to invCount.
        """
        inversion, ordenado = self.__sortAndCount(self.ranking)
        return inversion

    def __str__(self):
        """@note Print a ranking.
        """
        return str(self.ranking)

    def __Shuffle(self, a):
        """@note build a random list with n elements.
           @param[in] a a integer
           @return a list
           @retval list
        """
        # create array
        lista = [i for i in range(1, a+1)]
        for i in range(a-1, 0, -1):
            j = randint(0, i)
            lista[i], lista[j] = lista[j], lista[i]
        return lista

    def __sortAndCount(self, lista):
        """@note Create a sort list from two lists.
           @param[in] lista a list
           @return a list
           @retval list
        """
        if len(lista) <= 1:
            return 0, lista
        else:
            # Dividir para conquistar
            meioLista = int(len(lista) / 2)
            leftLista = lista[:meioLista]
            rightLista = lista[meioLista:]
            rA, leftLista = self.__sortAndCount(leftLista)
            rB, rightLista = self.__sortAndCount(rightLista)
            r, merge = self.__mergeAndCount(leftLista, rightLista)
            r += (rA + rB)
        return r, merge

    def __mergeAndCount(self, A, B):
        """@note Combine two lists and count inversions.
           @param[in] A a sort list
           @param[in] B a sort list
           @return inversion numbers , output list
           @retval integer
        """
        #Combina e conta as inversoes
        #A e B duas listas ordenadas
        #C lista de saida
        #i,j apontadores para cada lista, começando do início da lista
        #a_i, b_j elementos apontados por i,j
        #conta o numero de inversoes, valor inicial 0
        i, j = 0, 0
        inversion = 0
        C = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            elif B[j] < A[i]:
                C.append(B[j])
                j += 1
                inversion += (len(A) - i)
        C += A[i:]
        C += B[j:]
        return inversion, C