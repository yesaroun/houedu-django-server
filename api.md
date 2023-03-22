
# Courses

api/v1/courses/

- GET : 강의 리스트 (0)

api/v1/courses/<int>

- GET : 강의 디테일 

- POST : (생각해보기 수강 리스트에 넣는 기능! 이건 새로운 페이지 만들까 싶음)


# Reviews

api/v1/reviews/

- GET : 리뷰 리스트 (기본적인 정보는 다 가져왔는데 추가적으로 수강자들이 듣는 코스리스트 가져오기)
- POST : 리뷰 작성 (더 생각해보기)

api/v1/reviews/<int>
- GET : 리뷰 디테일 ? 필요?

api/v1/myreviews/ (X)
- GET : 내 리뷰들만 불러오기?
- POST : 리뷰 작성 (여기서 내 수강 리스트 불러올 수 있음)
- PATCH : 수정 가능할 듯

# Users

내 강의 목록 -> 이 시리얼라이즈 활용해서

내 리뷰 목록

내 리뷰 작성 페이지



여기에서 리뷰 작성, 삭제, 조회 만들기!


myinfo -> 닉네임 이메일, 회원 이미지 ... + 강의정보(내가 구매한 강의 - crsname)  
# myinfo/courses -> 수강 과목, 이름
myinfo/reviews -> 내가 작성한 리뷰 + 강의 정보(구매한 강의) (이미 작성했는지 여부는 더 고민하기)
