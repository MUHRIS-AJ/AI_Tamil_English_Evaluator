library(ggplot2)
library(dplyr)
data <- read.csv("labeled_results.csv")
summary <- data %>%
  summarise(
    Grammar = mean(grammar_score),
    Clarity = mean(clarity_score),
    Context = mean(context_score),
    Overall = mean(overall)
  )
print(summary)
df_long <- data %>%
  select(grammar_score, clarity_score, context_score) %>%
  tidyr::gather(key = "metric", value = "score")
ggplot(df_long, aes(x = metric, y = score, fill = metric)) +
  geom_boxplot() +
  ggtitle("AI Tamil–English Response Quality Metrics") +
  theme_minimal()
