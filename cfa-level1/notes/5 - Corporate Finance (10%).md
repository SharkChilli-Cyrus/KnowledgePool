# Corporate Finance (10%)

[TOC]

---

## Capital Budgeting

### Definition

The **capital budgeting process** is the process of identifying and evaluating capital projects, that is, projects where the cash flow to the firm will be received **over a period longer than a year**. => The process the companies use for decision-making on capital projects. - those projects with a life of **a year or more**.

* **4 Steps** in the capital budgeting process
    * Step 1: Generating ideas
    * Step 2: Analyzing project proposals (a cash flow forecast must be made)
    * Step 3: Create the firm-wide capital budget
    * Step 4: Monitoring decisions and conducting a post-audit

* **Categories** of capital budgeting projects
    * Replacement projectsaccompan
        * to maintain the business
        * for cost reduction - need detailed analysis
    * Expansion projects - need detailed analysis
    * New products or market development - need detailed analysis
    * Mandatory projects - for safety and environment
    * Other projects - R&D



### Principle

1. Decisions are based on **cash flows** <sup>incremental cash flows</sup>, <font color=red>not accounting income</font>.
    1. **Sunk costs** - are not affected by the accept/reject decision
    2. **Externalities** <sup>the effect the acceptance of a project may have on **other firm cash flows**</sup> - Cannibalization (negative) or Synergy (positive)
    3. **Conventional cash flow pattern** (the sign on the cash flows changes only once) and **Unconventional cash flow pattern** (more than one sign change)
2. Cash flows are based on opportunity costs
    1. **Opportunity costs** - be included in project costs
3. The timing of cash flows
4. Cash flows are analyzed on an **after-tax** basis
5. Financing costs are reflected in the project's required rate of return
    1. do not consider financing costs specific to the project when estimating incremental cash flows.



The **after-tax incremental cash flows** provide a sound basis for capital budgeting.

* **Include:**
    * Opportunity costs <sup> - the foregone return of the resource invests in the next-best project</sup>
    * Externalities <sup> - cannibalization (negative effect), synergy (positive effect)</sup>
* **Exclude:**
    * Sunk costs <sup> - decisions should not be affected by sunk costs (e.g. market research)</sup>
    * Financing costs <sup> - they are considered in discount rate (avoiding double counting problem)</sup>

* <font color=red>Timing value</font> of cash flows is crucial.



### Valuation

#### NPV - Net Present Value

**<font color=blue>The sum of the present value of all the after-tax cash flows of the project. NPV indicates the expected change in the value of the firm. </font>**

$NPV = CF_0 + \frac{CF_1}{(1+k)^1} + \frac{CF_2}{(1+k)^2} + \cdots + \frac{CF_n}{(1+k)^n}$

* <mark>Example</mark>

    Assume a project with following cash flows and cost of capital (discount rate) of 10%, calculate its NPV

    |  End of Year  |    0     |   1    |   2    |   3    |
    | :-----------: | :------: | :----: | :----: | :----: |
    |   Cash Flow   | -1000.00 | 200.00 | 400.00 | 800.00 |
    | Discounted CF | -1000.00 | 181.82 | 330.58 | 601.50 |

    $NPV = -1000 + \frac{200}{(1+10\%)^1} + \frac{400}{(1+10\%)^2} + \frac{800}{(1+10\%)^3} = 113.45$



* **Investment Decision Criteria** - for single/independent project
    * If NPV > 0, then accept/invest
    * If NPV < 0, then reject/not invest
* Advantages - Directly reflects the expect change of firm's value
* Disadvantages - <font color=red>Ignore the size of the project</font> (i.e. $CF_0 = -10,000$ or $CF_0 = -100$, the NPV might be same)



#### IRR - Internal Rate of Return

**<font color=blue>The discount rate that makes the total present value of all cash flows, the NPV, equal to zero. It is the expected return on the project.</font>**

$0=NPV= CF_0 + \frac{CF_1}{(1+IRR)^1} + \frac{CF_2}{(1+IRR)^2} + \cdots + \frac{CF_n}{(1+IRR)^n}$

* <mark>Example</mark>

    Assume a project has the following cash flows, calculate its IRR
    |  End of Year  |    0     |   1    |   2    |   3    |
    | :-----------: | :------: | :----: | :----: | :----: |
    |   Cash Flow   | -1000.00 | 200.00 | 400.00 | 800.00 |
    | Discounted CF | -1000.00 | 173.73 | 301.83 | 524.37 |

	$NPV = -1000 + \frac{200}{(1+IRR)^1} + \frac{400}{(1+IRR)^2} + \frac{800}{(1+IRR)^3} = 0 \Rightarrow IRR = 15.12\%$



* **Investment Decision Criteria** - for single/independent project
    * If IRR > cost of capital, then accept/invest
    * If IRR < cost of capital, then reject/not invest
* Advantages - It reflects the profitability
* Disadvantages:
    * Multiple and no IRR problem
    * Impractical assumption of reinvestment rate (IRR)
* Project Cash Flow Types
    * Conventional cash flows: cash flows change signs **once**
    * Nonconventional cash flows: cash flows change signs **more than once**
        * There may be multiple IRRs or no IRR

* Hurdle rate: the minimum IRR, projects with IRRs above this rate will be accepted



#### PBP - Payback Period

**<font color=blue>The number of years it takes to recover the initial cost of an investment.</font>** The payback period is **a measure of liquidity.**

* $PBP = A + \frac{B}{C}$
    * A: The last period with negative **cumulative** cash flow
    * B: The **absolute value** of cumulative cash flow at the end of the period
    * C: The cash flow during the period after A

* <mark>Example</mark>

    Assume a project has the following cash flows, calculate the payback period

    |     End of Year      |   0   |  1   |  2   |  3   |
    | :------------------: | :---: | :--: | :--: | :--: |
    |      Cash Flow       | -1000 | 200  | 400  | 800  |
    | Cumulative Cash Flow | -1000 | -800 | -400 | 400  |

    $PBP = 2+\frac{400}{800}=2.5$ Years



* **Investment Decision Criteria** - for single/independent project
* No decision rule like that of the NPV or IRR
* Advantages - simple and reflects the **liquidity**
* Disadvantages
    * Not a measure of value or profitability
    * Ignores time value of money and the risk of the project
    * Ignores cash flows beyond the payback period, which means terminal or salvage value would not be considered



#### DPB - Discounted Payback Period

<font color=blue>The number of years it takes for the cumulative **discounted** cash flows from a project to equal the original investment.</font> Must be greater than the payback period without discounting.

* $DPB=A+\frac{B}{C}$

    * A: The last period with negative cumulative discount cash flow
    * B: The absolute value of cumulative discount cash flow at the end of the period
    * C: The discount cash flow during the period after A

* <mark>Example</mark>

    Assume a project has the following cash flows and cost of capital of 10%, calculate the payback period

    |           End of Year           |   0   |    1    |    2    |   3    |
    | :-----------------------------: | :---: | :-----: | :-----: | :----: |
    |            Cash Flow            | -1000 |   200   |   400   |  800   |
    |      Discounted Cash Flow       | -1000 | 181.82  | 330.58  | 601.05 |
    | Cumulative Discounted Cash Flow | -1000 | -818.18 | -487.60 | 113.45 |

    $DPB = 2+\frac{487.60}{601.05}=2.8$ Years



**Discounted Payback Period (DPB)** always <font color=red>greater</font> than the **Payback Period (PBP)**.

* **Investment Decision Criteria** - for single/independent project
    * No decision rule like that of the NPV or IRR

* Advantages
    * Reflects the liquidity
    * Account for the time value of money and risk within the discounted payback period
* Disadvantages
    * Not a measure of value or profitability
    * Ignores cash flows beyond the discounted payback period



#### PI - Profitability Index

**<font color=blue>Present value of future cash flows divided by initial investment.</font>**

$PI=\frac{PV\ of\ Future\ CF}{CF_0}=1+\frac{NPV}{CF_0}$

It indicates the value you are receiving in exchange for one unit of currency invested.

* <mark>Example</mark>

    Assume a project has the following cash flows and cost of capital of 10%, calculate the profitability index

    |     End of Year      |   0   |   1    |   2    |   3    |
    | :------------------: | :---: | :----: | :----: | :----: |
    |      Cash Flow       | -1000 |  200   |  400   |  800   |
    | Discounted Cash Flow | -1000 | 181.82 | 330.58 | 601.05 |

    $PI=\frac{PV\ of\ future\ cash\ flows}{Initial\ investment}=\frac{181.82+330.58+601.05}{1000}=1.13$



* **Investment Decision Criteria** - for single/independent project
  
    * If PI > 1, then accept/invest
    * If PI < 1, then reject/not invest
* Advantage
    * It measures the profitability
    * It directly shows the amount of value created per unit of investment
* Disadvantage
  
    * The absolute NPV is ignored

> **NPV & IRR & PI** - For single/independent project, NPV, IRR and PI give the same accept/reject decisions
>
> If NPV  > 0, IRR > cost of capital, PI > 1, and vice versa
>
> If NPV  < 0, IRR < cost of capital, PI < 1, and vice versa



### NPV Profile

<font color=blue>A project's NPV profile is a graph that shows a project's **NPV for different discount rates**.</font>





### LOS

<font color=blue>**Q: Describe the capital budgeting process and distinguish among the various categories of capital projects**</font>

A: 



<font color=blue>**Q: Describe the basic principles of capital budgeting**</font>

A: 



<font color=blue>**Q: Explain how the evaluation and selection of capital projects is affected by mutually exclusive projects, project sequencing, and capital rationing**</font>

A: 



<font color=blue>**Q: Calculate and interpret new present value (NPV), internal rate of return (IRR), payback period, discounted payback period, and profitability index (PI) of a single capital project**</font>

A: 



<font color=blue>**Q: Explain the NPV profile, compare the NPV and IRR methods when evaluating independent and mutually exclusive projects, and describe the problems associated with each of the evaluation methods**</font>

A:



<font color=blue>**Q: Contrast the NPV decision rule to the IRR decision rule and identify problems associated with the IRR rule**</font>

A:



<font color=blue>**Q: Descrive expected relations among an investment's NPV, company value, and share price**</font>

A:



### Practice

**Q: The post-audit performed as part of the capital budgeting process is least likely to include the:**

* A: provision of future investment ideas
* B: rescheduling and prioritizing of projects
* C: indication of systematic errors

> **B**
>
> Rescheduling and prioritizing projects is part of the planning stage of the capital budgeting process, not the post-audit. The post-audit's purpose is to explain any differences between the actual and predicted results of a capital budgeting project. This process and aid in indicating systematic errors, improve business operations, and provide concrete ideas for future investment opportunities.



**Q: With regard to capital budgeting, an appropriate estimate of the incremental cash flows from a project is least likely to include:**

* A: externalities
* B: interest costs
* C: opportunity costs

> **B**
>
> Costs to finance the project are taken into account when the cash flows are discounted at the appropriate cost of capital, including interest costs in the cash flows would result in double-counting the cost of debt.



**Q: The post-audit is used to:**

* A: improve cash flow forecasts and stimulate management to improve operations and bring results into line with forecasts
* B: improve cash flow forecasts and eliminate potentially profitable but risky projects
* C: stimulate management to improve operations, bring results into line with forecasts, and eliminate potentially profitable but risky projects

> **A**
>
> A post-audit identifies what went right and what went wrong. It is used to improve forecasting and operations.



**Q: When computing the cash flows for a capital project, which of the following is least likely to be included:**

* A: Financing costs
* B: Opportunity costs
* C: Tax effects

> **A**



**Q: Which of the following statements describes the most appropriate treatment of cash flows in capital budgeting:**

* A: Interest costs are included in the project's cash flows to reflect financing costs
* B: A project is evaluated using its incremental cash flows on an after-tax basis
* C: Sunk costs and extemalities should not be included in the cash flow estimates

> **B**
>
> All of the incremental cash flows arising from a project should be analyzed on an after-tax basis.
>
> Sunk costs cannot be recovered once they have been incurred. Externalities (both positive and negative ones) are the effects of an investment decision on other things beside the investment itself, they should therefore be included in the cash flow estimation.
>
> Financing costs like interest costs are excluded from calculations of operating cash flows. The financing costs are reflected in the required rate of return for an investment project. If financing costs are included, we would be double-counting these costs.


