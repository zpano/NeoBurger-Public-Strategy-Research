# NeoBurger-Public-Strategy-Research

本次研究针对[NeoBurger Public Strategy](https://neoburger.github.io/strategy) -- GAS收益最大化的投资策略

## 研究概述

研究 NeoBurger-Public-Strategy 策略的不安全属性，寻找可能存在的低成本高影响(收益)的“攻击”，使得运用该投资策略的投资者无法得到预期的收益或无法收益。

## NeoBurger-Public-Strategy 策略概述

投资者发送NEO给

## 攻击评价指标

攻击需要投入的成本(包括不限于攻击所需要的NEO，GAS)-- Cost 

攻击影响的收益-- Unincome

攻击获取的收益(超过使用该投资策略的收益)-- Moreincome


## 可能的攻击

思路1:

自己成为节点，排挤掉最后一名的节点，按照此时的投票排行榜第21与22的排名来看需要640,829 - 623 = 640,206 NEO，影响收益为1/14。

思路2:

通过投票使得非理事会节点称为理事会节点，即投票使得原本排名第八的节点上升至第七，按照此时的投票数来看需要2,029,303 - 2,000,987 = 28,316 NEO，影响收益为1/14。

思路3:

通过某种手段使得共识节点异常，会导致替补进位，使得无法获取持续的收益。

思路4:

通过一些降低该投资的策略，使得投资者变换投票节点，消耗手续费超过收益或无法获取收益。

## 参考链接

[NEO 治理策略](https://neo.org/gov)

[NEO 投票](https://governance.neo.org/#/)





