# Beyond a Single Score: A Multi-Dimensional Evaluation Framework for Claims-Reserving Models

## Abstract

Claims-reserving model comparisons are often compressed into a single score or ranking. That compression is difficult to justify because reserving models produce central estimates, predictive distributions, uncertainty measures, responses to perturbations, and operational demands. This note asks how models should be evaluated when no metric represents all those properties. Drawing on Mack’s treatment of prediction uncertainty, England and Verrall’s review of stochastic reserving, Wüthrich and Merz’s separation of assumptions, prediction, and uncertainty, and Gneiting and Raftery’s theory of proper scoring rules, it proposes a multi-dimensional framework. The framework evaluates point accuracy, probabilistic quality, stability, uncertainty usefulness, and cost separately. It favors use-case-specific thresholds, a small metric set, and transparent Pareto or lexicographic comparison over arbitrary weighted averages. The contribution is methodological: a protocol for aligning evaluation with the reserving decision while preserving conflicts that a composite score would conceal.

## Research Question and Contribution

The research question is: **How should practitioners compare claims-reserving models when relevant performance criteria are heterogeneous and cannot be defensibly reduced to one universal scale?**

The supplied literature establishes why evaluation should extend beyond point estimates. Mack (1993) makes prediction uncertainty for chain-ladder reserves an explicit calculable object under stated assumptions. England and Verrall (2002) review stochastic methods and prediction-error considerations, supporting attention to distributional behavior and central estimates. Wüthrich and Merz (2012) distinguish assumptions, prediction, and uncertainty. Outside reserving specifically, Gneiting and Raftery (2007) show why probabilistic forecasts should be assessed with proper scoring rules that reward honest distributional reporting.

None of these sources proposes the exact framework below. The note’s contribution is to organize their bounded implications into a decision architecture with five dimensions and an explicit selection protocol. Model comparison becomes a constrained, multi-objective judgment. Aggregation is not neutral: a composite score embeds exchange rates among point error, tail behavior, runtime, and instability. Unless those rates arise from the actual decision, they are arbitrary.

## Literature-Grounded Evaluation Framework

The framework begins by identifying the forecast object required: a point reserve, predictive distribution, uncertainty measure, or combination. Evaluation then proceeds across five dimensions. The first three are grounded in the packet’s emphasis on prediction and uncertainty; stability and cost are proposed extensions connecting statistical evaluation to repeated operational use.

### Accuracy

Accuracy concerns the closeness of central predictions to subsequently observed outcomes. Appropriate measures depend on whether the target is an aggregate reserve, accident-year components, or another prespecified quantity. Absolute and squared-error forms answer different questions because they penalize large deviations differently. Scale-dependent errors may be meaningful within a stable portfolio, whereas comparisons across heterogeneous segments may require normalization chosen before results are inspected.

Point accuracy is necessary when decisions depend on a central estimate, but insufficient. Two models can have similar point errors while expressing materially different uncertainty, and a point metric cannot determine whether an associated predictive distribution is informative. The framework therefore reports accuracy as one coordinate, not as a proxy for overall quality.

### Calibration and Probabilistic Quality

When a model supplies a predictive distribution, evaluation should examine whether outcomes are compatible with assigned probabilities and whether the distribution is sufficiently informative. Calibration and concentration must be considered together: diffuse distributions may avoid conspicuous misses while offering little precision, whereas narrow distributions may systematically understate risk.

Gneiting and Raftery (2007) provide the basis for using strictly proper scoring rules. A proper score encourages honest predictive distributions rather than manipulation of dispersion to suit an unsuitable criterion. The framework requires at least one prespecified proper scoring rule whenever distributions are compared. Calibration diagnostics may accompany that score, but should not be collapsed into it. The aim is not a universally best distribution, but evidence that probabilistic performance is adequate for the stated task.

### Stability

Stability is the sensitivity of outputs and comparative standing to plausible changes in data, assumptions, or implementation choices. This dimension is proposed here rather than attributed to the cited sources. Checks may include controlled changes to the valuation sample, treatment of recent diagonals, segmentation, or model settings, provided they represent genuine application features rather than post hoc attempts to favor a model.

Stability is distinct from accuracy. A model may perform well in one window yet change sharply under a defensible specification change; stable estimates can also be persistently inaccurate. Reporting both prevents robustness from being inferred from one favorable realization. Stability measures should describe the magnitude and decision relevance of changes.

### Uncertainty

Uncertainty evaluation asks whether the model supplies information coherent with its assumptions, responsive to the data, and useful for the decision. Mack (1993) supports treating prediction uncertainty as an explicit object for chain-ladder reserves under stated assumptions. England and Verrall (2002) and Wüthrich and Merz (2012) likewise support evaluating prediction-error and uncertainty properties alongside central estimates.

This dimension should not prefer narrower intervals or smaller prediction errors automatically. Narrowness alone can reward understatement. Practitioners should examine the uncertainty object appropriate to the model and use case, its assumption dependence, and its relationship to probabilistic calibration. A method unable to provide required uncertainty information should be inadmissible for that use case rather than compensated by superior point accuracy.

### Computational and Operational Cost

Cost includes runtime, memory, implementation effort, data dependencies, specialist expertise, reproducibility, monitoring burden, and time required to explain or approve results. This is a proposed operational extension; the packet provides no comparative cost findings for particular methods. Cost matters because reserving is recurrent and subject to deadlines and governance constraints.

Cost should be measured in organization-relevant units, not vague labels such as “simple” or “complex.” A slower model may suit annual strategic work but fail rapid scenario analysis. Conversely, low computational cost does not excuse inadequate uncertainty reporting. Separate reporting makes such trade-offs visible.

## Decision Protocol for Metric Selection

Practitioners should select metrics before comparing model outputs.

1. **State the decision and horizon.** Specify the user, valuation target, update frequency, and consequences of error. A capital-oriented decision may require distributional and tail-sensitive assessment; rapid monitoring may impose strict latency constraints.
2. **Define the required forecast object.** Decide whether the decision requires a point estimate, full predictive distribution, uncertainty measure, or all three. This determines mandatory dimensions.
3. **Set admissibility conditions.** Establish non-compensable requirements, such as a required uncertainty quantity, reproducible execution within a deadline, or acceptable calibration diagnostics. Models failing a condition leave the candidate set.
4. **Choose one or a few metrics per dimension.** Each metric needs a stated interpretation and loss rationale. Use a proper score for distributions, a decision-relevant point-error measure, prespecified perturbations for stability, explicit uncertainty diagnostics, and observable resource measures for cost.
5. **Fix the evaluation design in advance.** Define targets, data partitions, perturbations, aggregation levels, and treatment of missing outcomes before results are known. This limits metric shopping.
6. **Compare profiles, not totals.** Identify dominance where one model is no worse on every required dimension and better on at least one. Where profiles cross, use lexicographic priorities or documented constraints. Apply weights only when stakeholders can defend them as actual trade-offs.
7. **Record residual judgment.** Document why the selected model’s weaknesses are acceptable, which alternatives remain credible, and what monitoring could trigger reconsideration.

The protocol does not eliminate judgment. It makes judgment inspectable and ties it to the use case rather than hiding it inside a formula.

## Limitations

The framework is conceptual and contains no empirical comparison, dataset, or numerical experiment. The packet supports the importance of stochastic prediction, proper scoring, and uncertainty, but not the effectiveness of the proposed stability tests, cost measures, admissibility rules, or Pareto procedure. Metric choices can still conflict, and claims outcomes may arrive slowly, limiting validation. Dependence among dimensions complicates interpretation: probabilistic scores reflect dispersion, while operational constraints may restrict feasible uncertainty methods. Finally, the protocol cannot supply organization-specific risk tolerances. Decision makers must state and revisit them as the portfolio and purpose change.

## Conclusion

Claims-reserving models should be evaluated as multi-attribute decision tools, not contestants in a universal ranking. The supplied literature justifies attention to prediction uncertainty and probabilistic forecasts beyond central estimates. Building on that foundation, this note proposes separate assessment of accuracy, probabilistic quality, stability, uncertainty, and operational cost. The practical discipline is to define the use case, impose non-compensable requirements, prespecify interpretable metrics, and compare profiles transparently. A single score is defensible only when its trade-offs genuinely represent the decision. Otherwise, preserving disagreement among dimensions is the information needed for responsible model selection.

## References

England, P. D., and R. J. Verrall. 2002. “Stochastic Claims Reserving in General Insurance.” *British Actuarial Journal* 8. https://doi.org/10.1017/S1357321700003809.

Gneiting, Tilmann, and Adrian E. Raftery. 2007. “Strictly Proper Scoring Rules, Prediction, and Estimation.” *Journal of the American Statistical Association* 102. https://doi.org/10.1198/016214506000001437.

Mack, Thomas. 1993. “Distribution-free Calculation of the Standard Error of Chain Ladder Reserve Estimates.” *ASTIN Bulletin* 23. https://doi.org/10.2143/AST.23.2.2005092.

Wüthrich, Mario V., and Michael Merz. 2012. *Stochastic Claims Reserving Methods in Insurance*. Wiley. https://doi.org/10.1002/9781119206262.