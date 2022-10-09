from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

What we need:
- For the top 3 Uniswap v3 pools, historical data for the different concentrated liquidity ranges:
this is, for each tick, the amount of asset locked by pair and their price.
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))



"""
## My thoughts:
*   I would use AWS S3 to store the data. It is a cheap and reliable storage solution.
*   I also would use AWS Redshift mainly because it is a columnar database and it is optimized for analytical workloads. It is also easy to scale. 
*   For orchestration, I would use Airflow. It is a great tool for scheduling and monitoring workflows. It is also easy to integrate with other AWS services. And job can run on the Elastic Container Service (ECS) or Elastic Kubernetes Service. Therefore, it is easy to scale up/out.
*   For realtime data processing, I would use AWS Kinesis. It is a fully managed service that can easily scale up/out. It is also easy to integrate with other AWS services such as AWS Redshift, Kinesis firehose or lambda.
*   For visualization, I would use Metabase. It is a great tool for data visualization.
*   In crypto, There are several different tools that can be used to extract data from the blockchain. For example, Infura, Etherscan, The Graph, etc. I would use The Graph because it is a great tool for querying the blockchain. 
"""

"""
## My code: https://github.com/0xmsu/streamlit-uniswap"""
