# 기말프로젝트 readme

## 1. 게임의 소개

### 제목: 포커디펜스 remaster

* **게임의 대한 정보** : 스타크래프트 유즈맵 포커디펜스 (하단 이미지 첨부)

![img](https://i.ytimg.com/vi/RXk4Ao6LtC0/hqdefault.jpg)

![Hand Combination 이미지](https://www.7luck.com/common/images/contents/img_threecard2.jpg)

* **게임의 목적** : 포커를 통해 디펜스에 필요한 유닛을 구매해서 스테이지를 깨는 방식
* **게임의 방법** : 라운드가 시작되기 전 포커를 한다. 포커는 5장을 받아 돈을 써서 2번에 걸쳐 카드를 바꿀 수 있고, 조커카드는 가장 높은 족보의 카드로 변환된다. 족보가 높은 순서대로 돈이나 성능이 좋은 유닛을 살수가 있게되고 돈으로 유닛을 업그래이드 하거나 전략적으로 배치해서 스테이지 마다 몰려오는 적들을 막는다.

<hr/>

## 2. GameState(Scene)의 수 및 각각의 이름

* **GameState의 종류** 
로고, 타이틀화면, 게임플레이씬, 스테이터스창(오버레이), 포커보드씬, 랭킹보드(오버레이)

## 3. 각 GameState별 항목 정리

```sequence
#GameState
TitleScene->GameScene: Start Button Click \nPress any key to continue
note over TitleScene: <End ,Start, Ranking button>
GameScene->TitleScene: Title Button Click \nPress any key to continue
note left of GameScene: Scene Change
note over GameScene: <Status, ranking, title button>, <Defenceboard>,\n<MyUnit>, <EnemyUnit>, <Upgrade button>
note over StatusWindow:<Player, Stage, Upgrade, \nMoney infomation><Ranking,Cencle Button>
GameScene->StatusWindow: Status Button click
StatusWindow->GameScene: Cencle Button click or Backspace
note right of GameScene: Overlay
note over PokerBoard: <5x1Card board><Card deck>\n<Reroll button>
GameScene->PokerBoard: PokerBoard Button click\n
PokerBoard->GameScene: Cencle Button click or Backspace
note right of GameScene: Scene Change
note over RankingBoard: <Cencle Button>\n<Ranking Infomation>
GameScene->RankingBoard: Ranking Button click
RankingBoard->GameScene: Cencle Button click or Backspace
note left of RankingBoard: Scene Change 
TitleScene->RankingBoard: Ranking Button click
RankingBoard->TitleScene: Cencle Button click or Backspace
```

## 4. 필요한 기술

* **다른과목에서 배운기술** : 윈도우API에서 오브젝트를 이동시키거나 충돌 판정 해보았다. 또한 간단한 게임들을 직접 구현해 보았다.
* **이 과목에서 배울것으로 기대되는 기술** : 클래스, 객체를 파이썬내에서 사용하는 기술들. 각종 게임 알고리즘들(충돌판정,이동 등).
  다양한 파이썬 라이브러리 함수들, 오브젝트들의 이미지를 다루는 기술(반전,회전 등)
* **다루지 않는거 같아서 요청할 기술** : bot이 사람이 하는것과 비슷하게 게임내에서 행동하는 기술, 
  화면 오버레이, 물체를 마우스로 클릭해서 놓을때 자석처럼 끌어당기는 효과가 생기는 기술.
