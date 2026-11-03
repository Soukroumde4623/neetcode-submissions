class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        lignes= [set() for _ in range(9)]
        colonnes =[set() for _ in range(9)]
        bloc = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j]=='.':
                    continue
                valeur = board[i][j]
                index_bloc =(i//3)*3+(j//3)

                if (valeur in lignes[i]
                    or valeur in colonnes[j] 
                    or valeur in bloc[index_bloc]):
                  
                    return False
                
                lignes[i].add(valeur)
                colonnes[j].add(valeur)
                bloc[index_bloc].add(valeur)

        return True

                