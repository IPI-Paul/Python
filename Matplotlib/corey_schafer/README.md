# Corey Schafer - MatPlotLib Tutorials

[Matplotlib Tutorial (Part 01): Creating and Customizing Our First Plots](https://youtu.be/UO98lJQ3QGI?si=E7jBTPjhOiuT1WTm) \
[Matplotlib Tutorial (Part 02): Bar Charts and Analyzing Data from CSVs](https://youtu.be/nKxLfUrkLE8?si=pm2O0PAuOjgfgGze) \
[Matplotlib Tutorial (Part 03): Pie Charts](https://youtu.be/MPiz50TsyF0?si=GtYT-VQ5cKDf0NGg) \
[Matplotlib Tutorial (Part 04): Stack Plots](https://youtu.be/xN-Supd4H38?si=XRiOdvpYXXvC2MJR) \
[Matplotlib Tutorial (Part 05): Filling Area on Line Plots](https://youtu.be/x0Uguu7gqgk?si=RwRnsBg8p1mUmjSb) \
[Matplotlib Tutorial (Part 06): Histograms](https://youtu.be/XDv6T4a0RNc?si=nulULpswalLJPvN5) \
[Matplotlib Tutorial (Part 07): Scatter Plots](https://youtu.be/zZZ_RCwp49g?si=NAki3kHBrKg9HXCk) \
[Matplotlib Tutorial (Part 08): Plotting Time Series Data](https://youtu.be/_LWjaAiKaf8?si=91yOXvtPN-fYjYzr) \
[Matplotlib Tutorial (Part 09): Plotting Live Data in Real-Time](https://youtu.be/Ercd-Ip5PfQ?si=flAWTE2ZyKK5rq2H) \
[Matplotlib Tutorial (Part 10): Subplots](https://youtu.be/XFZRVnP-MTU?si=sQwDj05YWc2w1yJK)

## Course Work

I suggested to someone high up in the Digital and Information team that it may be possible to use csv downloads from Tableau Visuals to test prediction models and display them using Python whilst testing. Problem was, I knew very little about producing charts in Python. After learning from a couple of other YouTube tutorials, Corey Schafer's tutorials offered more understanding and thankfully covered more ground.

- Corey covers each step in each tutorial to ensure that all is covered making sure you don't feel like you missed something.
- It was my intention to display all in a GUI eventually. So at first, I structured each class to contain the various examples shown using interactive console prompts.
- After completing all 10 tutorials, I implemented my best effort at Annotations/Tooltips. This meant changing the original structures slightly and I was not able to apply tooltips to all toturials.
- Then I implemented the GUI, an enhancement of the GUI I implemented for other course work.
- The only problem I had with the GUI was when one of the examples produced 2 figures and my setup only displays the first.
- Finally I implemented the right click context menu to be used when the output was a table of values.

### Interactive mode

```
python mpl_demo_01_line_plots.py
```

### GUI Mode

```
python display.py
```

## Tableau Findings

- Although I created a useful tool in Python that could be used to compared data in various csv files from Tableau Visual Downloads, there were some visuals that contained too much data to be downloaded.
- This meant that predictive models could only be applied when the data within the visual could be downloaded.
- The Tableau Data Quality checker tool is good for higlighting when filtering on one visual has not been applied in the same way as other visuals in the dashboard and can identify when a chart differs from a table or single metric.
- Other Tableau developers agree that the current Tableau prediction analysis does not offer them the ouputs they are looking for.
- I also tried out pantab. Like the problem with downloading a visual with too much data, connecting to a Tableau hyper file that is a few gigabytes in size freezes up my computer and uses up a lot of disk space then fails.
- Donwloading visuals with large datasets used 7-8GB memory and about 16GB of disk space before failing.

## Conclusion

There have been various views on whether predictive models should use aggregated data. To build predictive models from downloaded csv files of Tableau Visuals, one would need the dataset to be suitable for downloading either by being small in the first place or aggregated.
