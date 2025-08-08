import random

class RandomizedSet:
    def __init__(self):
        self.list = []
        self.dict = {}
        self.length = 0
        self.present = 0

    def insert(self, val):
        if not self.dict.get(val) == None:
            return False
        
        self.dict[val] = self.length
        self.list.append(val)
        self.present += 1
        self.length += 1
        return True

    def remove(self, val):
        if self.dict.get(val) == None:
            return False
            
        idx = self.dict[val]
        self.list[idx] = "empty"
        self.present -= 1
        return True

    def getRandom(self):
        if self.present == 0:
            return None
        
        while True:
            random_idx = random.randint(0, self.length - 1)
            if self.list[random_idx] != "empty":
                return self.list[random_idx]
    
    def size(self):
        return self.present


def performance_test():
    """대용량 데이터로 성능 테스트"""
    import time
    
    rs = RandomizedSet()
    n = 1000000
    
    # 삽입 성능 테스트
    start = time.time()
    for i in range(n):
        rs.insert(i)
    insert_time = time.time() - start
    
    
    # 삭제 성능 테스트
    start = time.time()
    for i in range(0, n, 2):  # 절반만 삭제
        rs.remove(i)
    remove_time = time.time() - start

    # 랜덤 샘플링 성능 테스트
    start = time.time()
    for i in range(n):
        rs.getRandom()
    random_time = time.time() - start
    
    length = rs.size()
    print(f"\n=== 성능 테스트 결과 (n={n}) ===")
    print(f"삽입 시간(n회): {insert_time:.4f}초")
    print(f"랜덤 샘플링 시간 (n회): {random_time:.4f}초")
    print(f"삭제 시간 (2/n회): {remove_time:.4f}초")
    print(f"최종 크기: {length}")

    print()
    print("채점 기준:") 
    print(f"삽입시간: 1초 이내: {insert_time:.4f}초")
    if insert_time < 1:
        print("성공")
    else:
        print("실패")
    print()

    print(f"삭제시간: 1초 이내: {remove_time:.4f}초")
    if remove_time < 1:
        print("성공")
    else:
        print("실패")
    print()

    print(f"랜덤 샘플링 시간: 1초 이내: {random_time:.4f}초")
    if random_time < 1:
        print("성공")
    else:
        print("실패")
    print()

    print(f"남은 원소 개수 500000개:  {length}")
    if length == 500000:
        print("성공")
    else:
        print("실패")


if __name__ == "__main__":
    performance_test()