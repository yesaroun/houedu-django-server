
# HouEdu Project

### 목차

- [프로젝트 요약](https://github.com/yesaroun/houedu-django-server#프로젝트-요약)
- [팀 노션 페이지](https://github.com/yesaroun/houedu-django-server#반장님들-팀-노션-페이지)
- [Database 구조](https://github.com/yesaroun/houedu-django-server#database-구조)
- [Django Model](https://github.com/yesaroun/houedu-django-server#django-model)
  - [Users Model](https://github.com/yesaroun/houedu-django-server#users-model)
- [API 설계 및 구조](https://github.com/yesaroun/houedu-django-server#api-설계-및-구조)
<hr>

## 프로젝트 요약
### 기간
2023.03.03 ~ 2023.03.29

### 기술 스택
- HTML 
- SCSS
- React
- Django
- Django Rest Framework
- uWSGI
- NGINX
- PHP
- Laravel
- Apache

### 협업 방식
- 피그마
- Git
- Slack
- Notion

### 팀원 역할 분담
이윤태(팀장)
- DB 설계 및 구현
- AWS(EC2, S3, RDS) 구축
- Django 서버 API 설계 및 구현
  - 로그인, 회원가입, 회원정보 수정, 비밀번호 수정
  - 강의 리스트, 강의 디테일
  - 리뷰 리스트, 리뷰 작성, 리뷰 삭제
- uWSGI, NGINX를 통한 서버 구축

임창섭
- 강의 리스트 페이지 구현
- 강의 디테일 페이지 구현

조다희
- Figma
- SCSS Base Setting
- 메인 페이지 구현
- 회원가입, 로그인, 카카오, Github 로그인 구현, 닉네임, 비밀번호 수정 페이지 구현
- 전체 리뷰 페이지 구현
- My 리뷰 페이지 구현
- axios api 연결

박정건
- DB 설계 및 구현
- AWS S3 스토리지 연동
- 강의실 프론트엔드/백엔드 개발

<hr>

<hr>

# 반장님들 팀 노션 페이지
[반장님들 팀 노션 페이지 링크](https://www.notion.so/deb717d82b634170ab7563cb0f6fd8c5)



# Database 구조

## 최종 DB

![img.png](md-img/img.png)

이번 프로젝트는 애자일(Agile) 프로세스로 진행되었습니다.

그래서 한 주기가 끝날때마다 DB 모델이 수정되었습니다.

---

## Version 1

![img_1.png](md-img/img_1.png)

가장 기초적으로 설계된 데이터베이스 입니다.

온라인 강의 웹 서비스에서 가장 핵심이라고 생각되는 user, 강사, course, lecture, 리뷰를 먼저 구현하였습니다.

여기서 ‘course’는 큰 분류의 강의이고, lecture는 큰 분류 강의(course)의 하위 강좌들입니다.

예를 들어 ‘인테리어 강의’는 ‘course’에 해당되고 ‘인테리어 강의 1강’, ‘인테리어 강의 2강’, … 와 같은 하위 강좌들은 ‘lecture’에 해당됩니다.

---

## Version 2

![img_2.png](md-img/img_2.png)

기본적인 기능을 구현한 이후, 설계된 데이터베이스입니다.

user의 구매 여부를 확인하는 ‘user_course’테이블과 유저가 강의를 시청했는지 여부를 확인하는 ‘video_watches’ 테이블이 추가되었습니다.

---

## Version 3

![img_3.png](md-img/img_3.png)

‘category’ 테이블이 추가 되고, ‘course’, ‘teacher’ 테이블의 컬럼들이 추가 되었습니다.

‘category’ 테이블을 추가해 카테고리별 분류 기능을 추가하였습니다.

‘course’와 ‘teacher’테이블에 기존에 있던 crs_info 컬럼처럼 기본적인 코스에 관한 정보뿐만 아니라 crs_goal(코스 목적), tcr_career(선생님 커리어) 등과 같은 추가적인 정보를 넣을 수 있는 컬럼을 추가했습니다. 

왜냐하면 저희가 구현하는 강의 디테일 페이지의 경우는 강의 정보를 하나의 이미지 파일로 넣는 일반적인 방식이 아닌, 직접 파트를 나눠 구현하다 보니, 상세 정보를 직접 다룰 필요가 있었습니다. 그래서 해당하는 데이터를 저장할 컬럼을 나누었습니다.

---


# Django Model

User모델의 경우 django의 AbstractUser 기능을 이용하기 위해 django model을 활용해 테이블을 만들었고, User 모델을 migrate한 이후에 다른 테이블들은 MySQL 쿼리문을 이용해 생성되었습니다.

또한 모든 필드에 help_text 속성을 사용하고, docstring과 type hint를 통해 가독성을 높였습니다.

클래스에는 One-Line Docstring을 적용하였고, method에는 Multi-Line Docstring을 적용했고 그 중에서도 Sphinx Style을 적용하였습니다.

## 세팅

> settings.py
> 

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "houedu_v2",
        "USER": "admin",
        "PASSWORD": env("DATABASE_PWD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": "3306",
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_ALL_TABLES'"},
    }
}
```

**DATABASE** : 데이터 베이스 연결에 대한 세부 정보를 dictionary 타입으로 저장

**ENGINE** : 연결에 사용할 데이터베이스 엔진 지정. 이 경우는 MySQL

**PASSWORD** : db 비밀번호, 이 경우는 env() 함수를 통해서 환경 변수의 값을 검색하도록 처리.

**"init_command": "SET sql_mode='STRICT_ALL_TABLES'"**

- “init_command” 옵션은 SQL 모드를 “STRICT_ALL_TABLES” 로 설정했습니다.
- “init_command” 옵션은 DB 연결이 설정된 직후 실행되어야 하는 명령을 지정하는 데 사용됩니다.
- sql_mode는 DB가 SQL 구문 및 데이터 유효성 검사를 처리하는 방법을 지정하는 데 사용됩니다.
- ‘STRICT_ALL_TABLES’ : MySQL이 데이터베이스 테이블에 데이터를 삽입하거나 업데이트할 때 더 엄격한 유효성 검사 규칙을 적용
예를 들어 2월 31일 과 같은 유효하지 않은 날짜 거부 등 테이블에 대해 지정된 유효성 검사 규칙을 위반하는 경우 값을 거부합니다.
- **이렇게 옵션을 지정하면 DB에 올바르지 않은 데이터나 유효하지 않은 데이터가 삽입되거나 업데이트 되어 데이터가 손상되는 것을 방지할 수 있습니다.**

## users Model

> users/models.py class User

```python
class User(AbstractUser):
    """
    사용자를 나타내는 모델
    """

    first_name: Text = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name: Text = models.CharField(
        max_length=150,
        editable=False,
    )
    nickname: Optional[Text] = models.CharField(
        unique=True,
        max_length=50,
        blank=True,
        null=True,
        help_text="닉네임 필드",
    )
    email: Text = models.EmailField(
        blank=False,
        unique=True,
        help_text="이메일 필드",
    )
    user_img: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="사용자 이미지 URL 필드",
    )

    class Meta:
        db_table = "user"

    def __str__(self) -> Text:
        """
        사용자의 문자열 표현 반환

        :return: 사용자 문자열
        """
        return f"{str(self.id)} {self.nickname}"
```

User 모델은 AbstractUser 모델을 상속받아 구현하였습니다. AbstractUser 클래스를 상속함으로써 Django의 인증 시스템에 내장된 암호 해싱 등과 같은 내장 보안 기능을 직접 구현하지 않고 활용할 수 있었습니다.

first_name과 last_name은 editable 속성을 False로 설정해 직접적인 편집을 할 수 없도록 처리하였습니다.

email, nickname 필드는 unique=True 제약 조건을 걸어 고유한 값이 되도록 하였습니다.

Meta 클래스의 db_table 옵션을 지정해서 테이블 명을 장고에서 정해주는 테이블 명이 아닌 제가 지정한 테이블 명을 사용했습니다. 

### Meta 클래스 관련해서 작성한 글

[Django Model에서의 Meta 클래스](https://yesaroun.tistory.com/entry/Django-Model에서의-Meta-클래스)


### [나머지 users model](https://github.com/yesaroun/houedu-django-server/blob/main/users/models.py)

다른 클래스들은 User 클래스와 비슷하며, 
조금 다른 점은 Meta 클래스의 옵션으로 ‘managed’를 사용해서 mysql 테이블을 직접 수정할 수있게 하였고, ‘verbose_name_plural’ 옵션을 추가해 장고 admin에서 확인할 수 있는 복수 명을 지정하였습니다.

```python
class VideoWatches(models.Model):
    """
    사용자가 시청한 동영상들을 나타내는 모델
    """
    
    # 중략
    
    class Meta:
        managed = True
        db_table = "video_watches"
        verbose_name_plural = "Video Watches"
```

- Teacher 클래스 : User의 계정이면서 추가적으로 Teacher 계정 정보를 갖을 수 있도록, user의 id를 FK로 갖습니다.
- UserCourse 클래스 : 수강 신청을 누르면 'user_course' 테이블에 user의 id와 course의 id를 왜래키로 받도록 하였습니다.

<hr>

## common Model

```python
class CommonModel(models.Model):
    """
    생성 및 업데이트 날짜와 시간을 나타내는 Common 필드
    """

    created_at: datetime = models.DateTimeField(
        auto_now_add=True,
        help_text="생성 날짜 및 시간",
    )
    updated_at: datetime = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        help_text="수정 날짜 및 시간",
    )

    class Meta:
        abstract: bool = True 
```

생성 시간과 수정 시간은 다른 클래스에서도 중복적으로 사용되기에 common app을 생성해서 추상 모델을 생성한 이후 다른 모델에서 상속받도록 설계하였습니다.

Meta 클래스의 abstract 속성을 True로 설정해 Django가 이 모델에 대한 DB 테이블을 생성하지 않도록 처리하였습니다.

<hr>

## courses Model

### Course class

```python
class Course(models.Model):
    """
    Course를 나타내는 모델
    """

    tcr: Optional[Teacher] = models.ForeignKey(
        "users.Teacher",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="courses",
        help_text="코스에 연간된 강사, 없는 경우 Null",
    )
    
    # 중략
    
    crs_content: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="코스 콘텐츠에 대한 정보, 없는 경우 Null",
    )

    class Meta:
        managed: bool = True
        db_table: str = "course"

    def __str__(self) -> Text:
        """
        코스 이름 반환
        :return: 코스 이름
        """
        return self.crs_name

    def count_reviews(self) -> int:
        """
        리뷰 수 세기
        :return: 리뷰 수
        """
        count: int = self.reviews.count()
        return count

    def rating(self) -> float:
        """
        코스의 평점 평균 계산
        :return: 코스 평균 평점
        """
        count = self.count_reviews()
        if count == 0:
            return 0.0
        else:
            total_rating: int = 0
            for review in self.reviews.all().values(
                "star"
            ):  # type: QuerySet[dict[str, int]]
                total_rating += review["star"]
            return round(total_rating / count, 2)
```
Course 모델에서 'count_reviews', 'rating' 메서드를 정의하였습니다.

이후에 설명할 serializers.py에서 활용되는 메서드들로, 'count_reviews'는 리뷰의 수를 리턴하고, 'rating'메서드는 'count_reivews'를 활용해서 코스의 리뷰 평균을 계산해 리턴합니다.

## reviews Model

### Review class

```python
class Review(CommonModel):
    """
    코스의 리뷰를 나타내는 모델
    """

    class StarChoices(models.IntegerChoices):
        """
        리뷰에서 별점을 정의하는 클래스
        """

        ONE_STAR = 1, _("★")
        TWO_STAR = 2, _("★★")
        THREE_STAR = 3, _("★★★")
        FOUR_STAR = 4, _("★★★★")
        FIVE_STAR = 5, _("★★★★★")

    # 중략
    
    star: Optional[int] = models.IntegerField(
        blank=True,
        null=True,
        choices=StarChoices.choices,
        help_text="리뷰 별점, 없으면 Null",
    )
    content: Text = models.TextField(
        help_text="리뷰 내용",
    )

    class Meta:
        managed: bool = True
        db_table: str = "review"

    def __str__(self) -> Text:
        """
        리뷰의 문자열 표현 반환
        :return: 리뷰 문자열
        """
        return f"{self.user}의 {self.crs} 리뷰"
```

Review 클래스에서 선언된 필드 중 star 필드는 choices 속성을 활용합니다. choices속성은 StarChoices클래스에 정의된 값만 허용하도록 합니다.

StarChoices 클래스는 정수만 저장할 수 있는 IntegerChoices 클래스를 상속받았고, 1~5사이의 정수값만 선택할 수 있도록 정의하였습니다.

# API 설계 및 구조

## test