
# 练习：map
实现 WordCount。它应当返回一个含有 s 中每个 “词” 个数的 map。函数 wc.Test 针对这个函数执行一个测试用例，并输出成功还是失败。
你会发现 strings.Fields 很有帮助。
https://tour.go-zh.org/moretypes/20

## 实现代码

```
package main

import (
    "golang.org/x/tour/wc"
    "strings"
)

func WordCount(s string) map[string]int {
    result := make(map[string]int)
    for _,val := range strings.Fields(s){
        v,_ := result[val]
        result[val] = v + 1
    }
    return result
}

func main() {
    wc.Test(WordCount)
}
```

## 运行结果

```
PASS
 f("I am learning Go!") = 
  map[string]int{"am":1, "learning":1, "Go!":1, "I":1}
PASS
 f("The quick brown fox jumped over the lazy dog.") = 
  map[string]int{"brown":1, "jumped":1, "lazy":1, "dog.":1, "The":1, "quick":1, "fox":1, "over":1, "the":1}
PASS
 f("I ate a donut. Then I ate another donut.") = 
  map[string]int{"donut.":2, "Then":1, "another":1, "I":2, "ate":2, "a":1}
PASS
 f("A man a plan a canal panama.") = 
  map[string]int{"A":1, "man":1, "a":2, "plan":1, "canal":1, "panama.":1}

```


# 练习：斐波纳契闭包
现在来通过函数做些有趣的事情。
实现一个 fibonacci 函数，返回一个函数（一个闭包）可以返回连续的斐波纳契数。
https://tour.go-zh.org/moretypes/23


## 实现代码

```
package main

import "fmt"

// fibonacci 函数会返回一个返回 int 的函数。
func fibonacci() func() int {
  i,j := 0,1
  return func() int{
    i,j = j,i+j
    return i
  } 
}

func main() {
  f := fibonacci()
  for i := 0; i < 10; i++ {
    fmt.Println(f())
  }
}
```

## 运行结果

```
1
1
2
3
5
8
13
21
34
55

```

# 练习：Stringers
让 IPAddr 类型实现 fmt.Stringer 以便用点分格式输出地址。
例如，IPAddr{1, 2, 3, 4} 应当输出 "1.2.3.4"。
https://tour.go-zh.org/methods/7

## 实现方法

```
package main

import "fmt"

type IPAddr [4]byte

// TODO: Add a "String() string" method to IPAddr.
func (ip IPAddr) String() string {
  return fmt.Sprintf("%v.%v.%v.%v", ip[0], ip[1], ip[2], ip[3])
}

func main() {
  addrs := map[string]IPAddr{
    "loopback":  {127, 0, 0, 1},
    "googleDNS": {8, 8, 8, 8},
  }
  for n, a := range addrs {
    fmt.Printf("%v: %v\n", n, a)
  }
}
```

## 运行结果

```
loopback: 127.0.0.1
googleDNS: 8.8.8.8

```
