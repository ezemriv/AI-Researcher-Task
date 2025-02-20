## Esto sobre porque no veo diferencias en el forecasting. Usar 10min timepoints tiene muy poca variabilidad
## de hecho por eso es tan bajo el MAE de KNN con MCAR, porque le es muy facil imputar


Yes, your observation is correct. The high-frequency nature of the 10-minute data means that consecutive timepoints are highly correlated, leading to small absolute differences between values. This results in:

Minimal Information Loss with Imputation:

Since variables change very little from one timestep to the next, standard imputation methods (e.g., KNN) can accurately reconstruct missing values.
The imputed dataset ends up closely resembling the original dataset.
No Impact on Forecasting Performance:

Since imputation does not introduce significant error, the forecasting model sees nearly identical inputs whether trained on the original or imputed dataset.
This explains why forecasting results remain unchanged.
Effect of Resampling on Variability:

As you increase the resampling interval (1-hour, 3-hour, etc.), the mean absolute differences also increase. This suggests that longer intervals introduce greater variability, making imputation potentially less accurate.
Possible Next Steps
Increase Missing Rate: Try a higher percentage of missing data to see when forecasting performance starts degrading.
Test on Lower-Frequency Data: Imputation might have a more noticeable effect at hourly or daily intervals, where variability is higher.
Use More Complex Imputation Models: If your goal is to evaluate imputation techniques, consider using LSTMs or probabilistic models that incorporate temporal structure.

