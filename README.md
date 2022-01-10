# NeoBurger-Public-Strategy-Research

本次研究针对[NeoBurger Public Strategy](https://neoburger.github.io/strategy) -- GAS收益最大化的投资策略

在已知确定的投策略下，通过恶意的投票，对该投资策略的收益造成影响。


[NEO 治理策略](https://neo.org/gov)
[NEO 投票](https://governance.neo.org/#/)


## 攻击危害系数f
攻击需要投入的NEO代币成本-- Cost

攻击影响的收益比例-- Influence

攻击危害系数f=Influence/Cost

简单例子：

假设我通过特定的投票使得该投资策略的收益下降1/14，此时付出的成本为10 NEO，则攻击危害系数为1/140

## 可能的攻击
思路1:

自己称为节点，排挤掉最后一名的节点，按照此时的投票排行榜第21与22的排名来看需要640,829 - 623 =640,206 NEO，影响收益为1/14

思路2:

通过投票使得非理事会节点称为理事会节点，即投票使得原本排名第八的节点上升至第七，按照此时的投票数来看需要2,029,303 - 2,000,987 = 28,316 NEO，影响收益为1/14






