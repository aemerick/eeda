

explain p-value
 --- have a technical answer
 --- have a non-technical answer

 run a regression, find p value is sig
    -- what?   p value is a regression represents slope tht is non-zero so if p is sigifincat than theere IS a correlation


Power analysis (3 thingss)
  1) Effect size
  2) alpha threshold
  3) "power" = how much power do you want for the test (80%/ 95%, etc.)
  Determines sample size


why do random sampling?
  - sampling
  - assignment -> don't want systematic group differences ()

doing some eda:
  - what if we notice we have missing data
  -

?? Little's test to check if things are missing? Are values missing at random?
Or are they missing for a biased reason? If fully random can be ok dropping vars

multi-colinearity -> high correlations in variables, inflates error, misestimate coeffs,
    - drop variables if high corr
    - Lasso, or ridge regression!!!!
    - PCA (rotation)
    - random forest tends to handle this better naturally
    - center variables (standardize)

For non-normal distributions: can bootstrap the sample!!!
   - KS tests

Can bias = "inability for model to capture true relationship"

Overfitting is happening!!!!
   - pruning!!
   - regularization
   - hyperparameter
   - more data!
   - early stopping criteria on training (nueral nets?)

ASSUMPTIONS OF LINEAR regression:
1) linear relatioship,
2) independence of obs
3) constant variance in residuals (homoscedascity)
4) normal residuals

Precision -> false positive rate (recommender system, crime prediction)
recall    -> false negative rate (smoke detector, medical)
