# Image Prompts for StatLearning Textbook

This file stores prompts for AI image generation to create illustrations for the StatLearning textbook.

---

## Chapter 1: Introduction to Statistical Learning and AI

### prompt: CH1_supervised_vs_unsupervised.png
**Description:** A clean educational diagram comparing Supervised Learning vs Unsupervised Learning, showing labeled data with arrows pointing to predictions on the left, and unlabeled data with arrows pointing to discovered patterns (clusters) on the right. Use a professional academic style with blue and orange color scheme.
**Suggested prompt:** "Clean academic diagram showing two panels side by side. Left panel labeled 'Supervised Learning' shows scattered data points with red and blue colors (labels) and arrows pointing to a decision boundary. Right panel labeled 'Unsupervised Learning' shows scattered gray data points clustering into two groups without predefined labels. Minimalist professional style, white background, clear labels in Thai or English."

### prompt: CH1_regression_vs_classification.png
**Description:** Side-by-side comparison showing regression (continuous values as a line through scattered points) and classification (discrete categories separated by a boundary). Clean educational style.
**Suggested prompt:** "Educational comparison diagram with two panels. Left panel shows 'Regression' with scattered dots on a plot and a straight trend line going through them, labeled 'Continuous Output'. Right panel shows 'Classification' with two groups of red and blue dots separated by a dashed line, labeled 'Discrete Categories'. Clean academic illustration style, white background."

### prompt: CH1_training_test_split.png
**Description:** Visual explanation of train/test split showing data being divided with a visual representation of the split ratio (e.g., 70/30 or 80/20).
**Suggested prompt:** "Educational diagram showing a large circle representing 'All Data' being split into two smaller circles labeled 'Training Set (70%)' and 'Test Set (30%)' with a scissors icon in the middle. Clean minimalist style, professional academic presentation."

### prompt: CH1_loss_function_visual.png
**Description:** Visual showing how a loss function measures prediction error, with a parabola showing the minimum point.
**Suggested prompt:** "Graph showing a U-shaped curve (parabola) representing a loss function with the vertical axis labeled 'Loss' and horizontal axis labeled 'Parameter'. A point marked at the bottom of the curve labeled 'Optimal'. Arrow annotations showing 'High Loss' at the top and 'Minimum Loss' at the bottom. Clean mathematical illustration style."

---

## Chapter 2: Supervised Learning Concepts

### prompt: CH2_overfitting_underfitting.png
**Description:** Three diagrams showing underfitting (straight line through curved data), good fit (smooth curve following data), and overfitting (wiggly line passing through every point).
**Suggested prompt:** "Three-panel educational diagram showing Underfitting, Good Fit, and Overfitting. Panel 1: A simple straight line failing to capture curved data pattern. Panel 2: A smooth curve that fits the data well. Panel 3: An excessively wiggly line that passes through every data point exactly. Each panel clearly labeled. Clean academic style with different colored curves."

### prompt: CH2_gradient_descent_visual.png
**Description:** A 3D-like contour plot or 2D visualization showing gradient descent path toward the minimum of a loss function.
**Suggested prompt:** "Educational illustration of gradient descent optimization. A 2D contour plot with elliptical contours representing a loss function landscape, with arrows showing the path of gradient descent from the edge moving toward the center minimum point labeled 'Global Minimum'. Professional academic diagram style."

### prompt: CH2_bias_variance_tradeoff.png
**Description:** Visual showing the bias-variance tradeoff concept with a target (bullseye) analogy - high bias (far from center with tight clustering), good balance (near center), high variance (near center but scattered).
**Suggested prompt:** "Bullseye target diagram with three panels. Panel 1 'High Bias' shows all darts far from center but closely grouped. Panel 2 'Good Balance' shows darts close to center. Panel 3 'High Variance' shows darts scattered around but some near center. Clear labels, minimalist style."

---

## Chapter 3: Regression Analysis

### prompt: CH3_simple_linear_regression_example.png
**Description:** A scatter plot with a simple linear regression line, showing the concept of residuals (vertical distances from points to the line).
**Suggested prompt:** "Scatter plot with 15-20 data points showing a positive linear relationship between 'Hours Studied' on x-axis and 'Exam Score' on y-axis. A straight regression line passes through the data with small vertical dashed lines showing residuals. Point A marked at (6, 78) and line extended. Clean educational graph style."

### prompt: CH3_logistic_s_curve.png
**Description:** S-curve (sigmoid) showing probability output from 0 to 1, with threshold line at 0.5.
**Suggested prompt:** "Sigmoid (logistic) curve graph showing probability from 0 to 1 on y-axis versus input variable on x-axis. A horizontal dashed line at y=0.5 represents the classification threshold. The S-curve approaches 0 on the left and 1 on the right, crossing the threshold at the midpoint. Labeled 'Sigmoid Function' and 'Threshold'. Clean mathematical style."

### prompt: CH3_confusion_matrix_visual.png
**Description:** A colorful 2x2 confusion matrix heatmap showing True Positive, True Negative, False Positive, False Negative.
**Suggested prompt:** "2x2 confusion matrix heatmap with four colored cells labeled: Top-Left 'True Negative (TN)', Top-Right 'False Positive (FP)', Bottom-Left 'False Negative (FN)', Bottom-Right 'True Positive (TP)'. Color gradient from light to dark blue. Clear grid lines, professional academic style."

---

## Chapter 4: Decision Trees and Random Forest

### prompt: CH4_decision_tree_example.png
**Description:** A simple decision tree diagram for a classification problem (e.g., approve loan) with rectangular decision nodes and leaf nodes showing outcomes.
**Suggested prompt:** "Simple decision tree diagram for loan approval. Root node asks 'Income > 50,000?', branching to left 'Has Collateral?' and right 'Credit Score > 700?'. Leaf nodes show 'Approve' or 'Reject' outcomes. Clean professional tree diagram style with rounded boxes for decisions and square boxes for outcomes."

### prompt: CH4_random_forest_ensemble.png
**Description:** Visual showing multiple decision trees combining their votes to produce a final ensemble prediction.
**Suggested prompt:** "Diagram showing 'Random Forest' concept with 5 small decision tree icons on the left, each with different branching patterns, connected by arrows to a central circle labeled 'Ensemble/Vote'. Final output arrow on right points to 'Final Prediction'. Clean professional illustration showing the bagging concept."

### prompt: CH4_entropy_information_gain.png
**Description:** Visual showing entropy calculation and information gain, with pie charts showing before and after split impurity.
**Suggested prompt:** "Educational diagram showing entropy and information gain. Left side: single pie chart with 50% red and 50% blue (entropy = 1.0). Right side: two pie charts after split, left with 80% red 20% blue, right with 20% red 80% blue. Arrow labeled 'Information Gain' between them. Clean academic style."

### prompt: CH4_tree_pruning.png
**Description:** Before and after comparison showing a complex overfitting tree being pruned to a simpler version.
**Suggested prompt:** "Two decision trees side by side. Left tree is tall and complex with many branches (overfitting). Right tree is shorter and simpler (pruned). Dashed scissors icon in the middle between them. Labels 'Before Pruning' and 'After Pruning'. Clean professional style."

---

## Chapter 5: Naive Bayes

### prompt: CH5_bayes_theorem_visual.png
**Description:** Visual representation of Bayes' theorem with probability areas showing prior, likelihood, and posterior.
**Suggested prompt:** "Bayes theorem visualization with two overlapping circles. Circle A labeled 'P(B|A)' and circle B labeled 'P(A|B)'. Mathematical formula P(A|B) = P(B|A)P(A) / P(B) displayed below. Clean educational diagram with clear mathematical notation style."

### prompt: CH5_naive_bayes_classification.png
**Description:** Simple illustration showing how Naive Bayes combines feature probabilities to make a classification decision.
**Suggested prompt:** "Diagram showing Naive Bayes classification process. Left side shows three feature icons (email icon, calendar icon, dollar icon) representing email features. Arrows point to center showing 'P(Class|Features) = P(Feature1|Class) × P(Feature2|Class) × P(Feature3|Class)'. Right side shows two output paths labeled 'Spam' and 'Not Spam'. Clean professional style."

---

## Chapter 6: Unsupervised Learning

### prompt: CH6_kmeans_step_by_step.png
**Description:** Four-panel diagram showing K-Means iteration: initial random centroids, assignment step, update step, and final clusters.
**Suggested prompt:** "Four-panel educational diagram showing K-Means algorithm steps. Panel 1: 20 scattered points with 3 large star markers as initial random centroids. Panel 2: Same points colored into 3 groups by nearest centroid with lines connecting to centroids. Panel 3: Centroids moved to mean position of assigned points (shown with arrows). Panel 4: Final clean clusters with centroids at centers. Clean academic style."

### prompt: CH6_hierarchical_clustering_dendrogram.png
**Description:** A dendrogram showing hierarchical clustering with 5-6 data points being progressively merged.
**Suggested prompt:** "Dendrogram diagram showing hierarchical clustering of 5 data points (A, B, C, D, E) at the bottom. Horizontal lines connect points as they merge at increasing heights. Y-axis labeled 'Distance'. Clean tree structure showing the hierarchy clearly."

### prompt: CH6_pca_visualization.png
**Description:** 3D to 2D dimensionality reduction visualization showing principal component projection.
**Suggested prompt:** "Two-panel diagram. Left panel shows 3D scatter plot of data points distributed in an elongated ellipsoid shape. Right panel shows 2D projection onto the principal plane with axis labels 'PC1' and 'PC2'. Arrows showing the direction of maximum variance. Clean academic style."

### prompt: CH6_dbscan_clustering.png
**Description:** DBSCAN clustering result showing core points, border points, and noise/outlier points.
**Suggested prompt:** "DBSCAN clustering result showing three clusters of different colors (blue, green, orange) and red X marks for outliers/noise points. A few points labeled 'Core', 'Border', and 'Outlier'. Clear density-based clustering visualization."

---

## Chapter 7: Model Evaluation

### prompt: CH7_cross_validation_kfold.png
**Description:** K-Fold cross-validation visualization showing data being split into K=5 folds with rotation of test set.
**Suggested prompt:** "5-Fold Cross-Validation diagram. A rectangle divided into 5 equal vertical sections labeled Fold 1 through Fold 5. Below it, 5 rows show which fold is the test set (highlighted) and which are training sets (shaded). Rotation arrows or clear indication that each fold takes turns being the test set. Clean educational style."

### prompt: CH7_roc_curve.png
**Description:** ROC curve graph showing the trade-off between True Positive Rate and False Positive Rate, with AUC shaded area.
**Suggested prompt:** "ROC curve graph with diagonal reference line labeled 'Random Classifier' and a curved line above it labeled 'Our Model'. X-axis 'False Positive Rate (1 - Specificity)' from 0 to 1, Y-axis 'True Positive Rate (Sensitivity)' from 0 to 1. AUC (Area Under Curve) shaded area labeled. Point marked at optimal threshold. Clean professional academic style."

### prompt: CH7_precision_recall_curve.png
**Description:** Precision-Recall curve showing the trade-off between precision and recall for different thresholds.
**Suggested prompt:** "Precision-Recall curve graph. X-axis 'Recall' from 0 to 1, Y-axis 'Precision' from 0 to 1. A smooth descending curve labeled 'PR Curve'. Point marked at the elbow or optimal operating point. Clean professional academic graph style."

### prompt: CH7_learning_curve.png
**Description:** Learning curve showing training and validation error vs training examples, diagnosing overfitting vs underfitting.
**Suggested prompt:** "Learning curve graph. X-axis 'Number of Training Examples' from 0 to 1000, Y-axis 'Error' from 0 to 100%. Two curves: training error (blue, starts low and increases) and validation error (orange, starts high and decreases). Labels 'High Variance (Overfitting)' and 'High Bias (Underfitting)' regions marked. Clean educational style."

---

## Additional Prompts

### prompt: CH7_confusion_matrix_multiclass.png
**Description:** Confusion matrix for multi-class classification (3x3 or 4x4) showing misclassification patterns.
**Suggested prompt:** "3x3 confusion matrix heatmap for multi-class classification. Rows labeled 'Actual: A, B, C', columns labeled 'Predicted: A, B, C'. Diagonal cells dark colored (correct), off-diagonal cells lighter with numbers. Color gradient from dark to light blue. Professional academic style."

### prompt: CHX_feature_importance_rf.png
**Description:** Bar chart showing feature importance scores from a Random Forest model.
**Suggested prompt:** "Horizontal bar chart showing feature importance. Y-axis lists features: 'Age', 'Income', 'Credit Score', 'Employment Years', 'Debt Ratio'. X-axis shows importance score from 0 to 0.5. Bars sorted from longest (most important) to shortest. Clean professional style."

---

*Last updated: 2026-05-01*
*Project: StatLearning Textbook - Thai Statistical Learning Book*
