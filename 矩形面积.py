class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        def fun(A,B,C,D,E,F,G,H):
            if A>E:  #将第一个矩形放左边
                return fun(E,F,G,H,A,B,C,D)
            if C<E or H<B or F>D: #不重叠
                return (C-A)*(D-B)+(G-E)*(H-F)
            #      (高（上边界-下边界）)*(宽（右边界-左边界）)
            area=(min(D,H)-max(B,F))*(min(C,G)-max(E,A))
            return (C-A)*(D-B)+(G-E)*(H-F)-area
        return fun(A,B,C,D,E,F,G,H)

