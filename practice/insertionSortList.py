class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        out = head ###把頭設為out去後面比
        head = head.next###因此原本頭的下一個就變成頭了
        tail = out####再把拿去後面比的out變成新的排列好的序列的頭
        #####三種狀況1)拿去比的小於新序列的頭2)大於新序列的頭3)大於頭小於中間的要一個一個比
        while head:
            temp = head
            head = head.next
            if temp.val <= out.val:#######情況一
                temp.next = out
                out = temp
            elif temp.val >= tail.val:#####情況二
                tail.next = temp
                tail = temp
            else:####接著一個一個走訪
                it = out
                while it.next != tail and it.next.val < temp.val:
                    it = it.next
                temp.next = it.next#####要連結上
                it.next = temp
        tail.next = None
        return ou
