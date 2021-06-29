"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""
class Ordenacao():
    def __init__(self, array_para_ordenar: list):
        self.my_array = array_para_ordenar

    # def __repr__(self) -> str:
    #     return "isso não é oq vc esperava?"

    # def __str__(self) -> str:
    #     return "isso não é oq vc esperava?"

    def _partition(self, arr: list, low: int, high: int) -> int:
        i = (low-1)         # index of smaller element
        pivot = arr[high]     # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:

                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def _quickSort(self, arr: list, low: int, high: int) -> None:
        if len(arr) == 1:
            return arr
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self._partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self._quickSort(arr, low, pi-1)
            self._quickSort(arr, pi+1, high)

    def ordena(self) -> list:
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        n = len(self.my_array)
        self._quickSort(self.my_array, 0, n-1)
        return self.my_array

    def toString(self) -> str:
        """Converte o conteudo do self.my_arrayay em String formatado
           Exemplo: 
           Para o conteudo do self.my_arrayay: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do self.my_arrayay formatado
        """   
        return ','.join(map(str, self.my_array))

ordenacao = Ordenacao([1,2,3,4])
print(ordenacao)