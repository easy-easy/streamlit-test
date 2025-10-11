"""DataFrame demo implementation module.

This module contains all the business logic for the DataFrame demo page,
separated from the page layout and UI configuration.
"""

from urllib.error import URLError

import altair as alt
import pandas as pd
import streamlit as st


@st.cache_data
def get_un_data() -> pd.DataFrame:
    """Fetch UN agricultural data from S3 bucket.

    Returns:
        pd.DataFrame: Agricultural data indexed by Region.

    """
    aws_bucket_url = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(aws_bucket_url + "/agri.csv.gz")
    return df.set_index("Region")


def create_area_chart(data: pd.DataFrame) -> alt.Chart:
    """Create an area chart from the provided data.

    Args:
        data: DataFrame with columns 'year', 'Gross Agricultural Product ($B)', and 'Region'.

    Returns:
        alt.Chart: Altair area chart object.

    """
    chart = (
        alt.Chart(data)
        .mark_area(opacity=0.3)
        .encode(
            x="year:T",
            y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
            color="Region:N",
        )
    )
    return chart


def prepare_chart_data(df: pd.DataFrame, countries: list[str]) -> pd.DataFrame:
    """Prepare data for charting by filtering, scaling, and transforming.

    Args:
        df: Source DataFrame indexed by Region.
        countries: List of country names to include.

    Returns:
        pd.DataFrame: Transformed data ready for charting.

    """
    data = df.loc[countries]
    data /= 1000000.0  # Convert to billions

    # Transform for charting
    data = data.T.reset_index()
    data = pd.melt(data, id_vars=["index"]).rename(
        columns={"index": "year", "value": "Gross Agricultural Product ($B)"},
    )
    return data


def render_dataframe_demo():
    """Render the DataFrame demo.

    This function contains all the UI logic and coordinates the data fetching,
    processing, and visualization components.
    """
    try:
        # Fetch data
        df = get_un_data()

        # User input
        countries = st.multiselect(
            "Choose countries",
            list(df.index),
            ["China", "United States of America"],
        )

        if not countries:
            st.error("Please select at least one country.")
            return

        # Display raw data table
        display_data = df.loc[countries] / 1000000.0
        st.subheader("Gross agricultural production ($B)")
        st.dataframe(display_data.sort_index())

        # Prepare and display chart
        chart_data = prepare_chart_data(df, countries)
        chart = create_area_chart(chart_data)
        st.altair_chart(chart, use_container_width=True)

    except URLError as e:
        st.error(f"This demo requires internet access. Connection error: {e.reason}")
