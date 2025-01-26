class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row_list = [row for row in image]
        row_inv = []
        
        for i in range(len(row_list)):
           row_inv.append(row_list[i][::-1])
           i += 1
        
        row_img = []
        for row in row_inv:
            new_row = []
            for val in row:
                if val == 1:
                    new_row.append(0)
                else:
                    new_row.append(1)
            row_img.append(new_row)
                
        return row_img
       
        
