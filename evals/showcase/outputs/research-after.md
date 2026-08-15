# Beyond a Single Score: A Multi-Dimensional Evaluation Framework for Claims-Reserving Models

## Abstract

Claims-reserving model evaluation is often framed as a contest producing a single winner. That framing is inadequate when models serve different decisions and produce objects ranging from point estimates to full predictive distributions. This note asks how reserving models should be compared without reducing distinct dimensions to an arbitrary composite score. Drawing on literature concerning chain-ladder prediction uncertainty, stochastic reserving, and proper scoring rules, it proposes a five-dimensional framework: point accuracy, calibration and probabilistic quality, stability, uncertainty representation, and computational or operational cost. The framework is an original decision structure, not a result attributed to the cited literature. Models are screened against use-case-specific requirements and then compared through a declared vector of metrics, with trade-offs reported rather than concealed by weights. The conclusion is that model selection is defensible only relative to a stated purpose.

## Research Question and Contribution

The research question is: **How should actuarial practitioners evaluate claims-reserving models when relevant qualities are distinct, partly non-substitutable, and dependent on intended use?** A scalar ranking can make unlike deficiencies appear exchangeable. A gain in point accuracy might numerically offset poor distributional performance, unstable estimates, or an operational burden, even when the use case makes one weakness unacceptable.

The literature establishes a basis for resisting that reduction. Mack (1993) treats prediction uncertainty for chain-ladder reserve estimates as an object requiring explicit calculation under stated assumptions. England and Verrall (2002) review stochastic reserving methods and prediction-error considerations, placing central estimates within a wider predictive problem. Wüthrich and Merz (2012) distinguish assumptions, prediction, and uncertainty in stochastic claims reserving. Gneiting and Raftery (2007) explain why probabilistic forecasts should be assessed with proper scoring rules that reward honest predictive distributions. None proposes the exact framework below. This note translates their shared implication—that point estimates and predictive uncertainty are different objects—into an evaluation architecture that also makes stability and implementation cost visible.

## A Literature-Grounded Evaluation Framework

The proposed framework represents each candidate model by a performance vector:

\[
E(M) = (A, P, S, U, C),
\]

where \(A\) denotes point accuracy, \(P\) probabilistic quality, \(S\) stability, \(U\) uncertainty representation, and \(C\) computational or operational cost. The notation does not imply equal importance, common units, or compensability. It requires each dimension to be interpreted separately.

**Accuracy.** Point accuracy concerns how closely a model's central reserve prediction corresponds to subsequently observed outcomes under a specified validation design. Measures may express absolute or relative error, but the choice must match the decision's loss structure. A metric that heavily penalizes large misses answers a different question from one giving proportional influence to each origin period or segment. Accuracy also requires a declared aggregation level: total reserve accuracy can conceal offsetting errors, while granular accuracy may overemphasize immaterial cells. The prediction target and aggregation rule should therefore be fixed before results are examined.

**Calibration and probabilistic quality.** When a model supplies a predictive distribution, point error discards much of its output. Gneiting and Raftery (2007) support using strictly proper scoring rules, which reward predictive distributions that truthfully express the forecaster's beliefs. In this framework, a proper score is the primary comparative measure of probabilistic quality. Calibration diagnostics separately check whether realized outcomes are compatible with stated probabilities or intervals. The two are not interchangeable: calibration examines statistical consistency, whereas a proper score evaluates the distribution as a whole. This distinction is the note's synthesis, not an attributed reserving result.

**Stability.** Stability asks whether conclusions change materially under defensible perturbations to information or specification: advancing the valuation date, modifying a small number of observations, changing a reasonable modelling choice, or examining adjacent segments. The statistic might track variation in the central estimate, predictive quantiles, model selection, or management action. Stability is not accuracy; a model can perform well in one validation sample yet be highly sensitive to modest changes. Nor should stability mean immobility. Estimates should respond to genuine information. Evaluation should identify disproportionate sensitivity and its source.

**Uncertainty.** Mack (1993), England and Verrall (2002), and Wüthrich and Merz (2012) support treating prediction uncertainty as a first-class reserving concern. This framework separates uncertainty representation from probabilistic scoring because practitioners must determine what uncertainty a model represents, which assumptions support it, and whether the reported quantity matches the decision horizon. Evaluation should document the uncertainty output, its assumptions, and the behavior of intervals or tail quantities under validation and sensitivity analysis. A narrow interval is not inherently preferable; apparent precision without adequate probabilistic support can mislead.

**Computational and operational cost.** This dimension is proposed on decision grounds rather than derived from a claim in the sources. It includes runtime, implementation and maintenance effort, data preparation, reproducibility, governance, and the ability to rerun the process within the reserving timetable. These components should remain separate unless the organization has a defensible common valuation. Some are constraints: a model that cannot be validated, governed, or executed on schedule may be unusable regardless of statistical performance. Others are direct trade-offs, such as additional runtime for richer uncertainty output.

## Decision Protocol for Metric Selection

Practitioners can apply the framework through six ordered decisions.

1. **State the use case and action.** Specify whether the output supports a central booked estimate, distribution-sensitive risk assessment, model monitoring, or recurring production. Name the decision-maker, horizon, portfolio level, and consequence of error.

2. **Define the forecast object.** Decide whether the model must provide a point, interval, selected quantiles, or full predictive distribution. Do not evaluate a distributional model only as a point predictor when its distribution motivates its use.

3. **Translate consequences into metric properties.** Choose point-error metrics according to the importance of large versus small errors, scale, and aggregation. For predictive distributions, select a strictly proper scoring rule consistent with the forecast object, following Gneiting and Raftery (2007). Add calibration diagnostics rather than treating them as substitutes.

4. **Set non-compensable thresholds.** Before observing comparative results, define minimum standards for dimensions the use case cannot trade away. These may include acceptable calibration behavior, maximum cycle time, reproducibility, or stability tied to management action. Thresholds should follow the decision, not preserve a favored model.

5. **Design validation and sensitivity checks.** Fix historical evaluation windows, aggregation levels, treatment of unavailable future observations, and perturbations used to examine stability. Record which uncertainty quantity is assessed and under which assumptions. Report relevant segments as well as aggregate results when offsetting errors matter.

6. **Select from the admissible set.** Eliminate models failing minimum requirements. For the remainder, present the metric vector and explicit trade-offs. If one model is no worse on every relevant dimension and better on at least one, it can be preferred for that use case. Otherwise, the decision-maker must state which dimension has priority. A hidden weighting scheme should not turn that judgment into a supposedly objective universal score.

## Limitations

This conceptual note uses a deliberately restricted source packet. It provides neither empirical evidence that the framework improves reserve decisions nor numerical guidance for thresholds, validation windows, or metrics. The literature supports explicit attention to stochastic prediction, proper probabilistic assessment, and reserve uncertainty, but does not validate the proposed five-part architecture. Stability and operational cost enter through decision analysis, not findings attributed to the sources.

The dimensions are not fully independent. Computational choices affect available uncertainty methods; unstable estimates can worsen probabilistic scores; and validation design shapes every comparison. Separate reporting makes these interactions visible but does not remove them. Historical validation may also be weak where portfolios, claims processes, or operating conditions change. Metric results then require contextual judgment rather than mechanical extrapolation.

## Conclusion

Claims-reserving models should be selected for a specified actuarial decision, not ranked as if one scalar measure captured every relevant virtue. The supplied literature supports separating central prediction from probabilistic assessment and explicit uncertainty analysis. Building on that foundation, this note proposes evaluating accuracy, probabilistic quality, stability, uncertainty representation, and operational cost as a vector. Practitioners should choose metrics from the forecast object and consequences of error, establish non-compensable requirements in advance, validate at decision-relevant levels, and disclose trade-offs among admissible models. The outcome is not a universal champion, but a selection whose rationale is visible, contestable, and aligned with its use.

## References

England, P. D., and R. J. Verrall. 2002. “Stochastic Claims Reserving in General Insurance.” *British Actuarial Journal* 8. https://doi.org/10.1017/S1357321700003809.

Gneiting, T., and A. E. Raftery. 2007. “Strictly Proper Scoring Rules, Prediction, and Estimation.” *Journal of the American Statistical Association* 102. https://doi.org/10.1198/016214506000001437.

Mack, T. 1993. “Distribution-free Calculation of the Standard Error of Chain Ladder Reserve Estimates.” *ASTIN Bulletin* 23. https://doi.org/10.2143/AST.23.2.2005092.

Wüthrich, M. V., and M. Merz. 2012. *Stochastic Claims Reserving Methods in Insurance*. Wiley. https://doi.org/10.1002/9781119206262.