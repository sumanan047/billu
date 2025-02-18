import pytest
from pylogo.distributions import Distribution_1D, Distribution_2D

def test_distribution_1d_uniform():
    dist = Distribution_1D()
    dist.uniform(low=0, high=1, size=100)
    assert len(dist.data) == 100
    assert all(0 <= x <= 1 for x in dist.data)

def test_distribution_1d_normal():
    dist = Distribution_1D()
    dist.normal(mean=0, std=1.0, size=100)
    assert len(dist.data) == 100
    # Check if data is approximately normally distributed (basic check)
    assert dist.data.mean() == pytest.approx(0, abs=0.5)  # Allow for some tolerance
    assert dist.data.std() == pytest.approx(1, abs=0.5)

def test_distribution_2d_uniform():
    dist = Distribution_2D()
    dist.uniform(low=[0, 0], high=[1, 1], size=100)
    assert len(dist.x_arr) == 100
    assert len(dist.y_arr) == 100
    assert all(0 <= x <= 1 for x in dist.x_arr)
    assert all(0 <= y <= 1 for y in dist.y_arr)

def test_distribution_2d_normal():
    dist = Distribution_2D()
    dist.normal(mean=[0, 0], cov=[[1, 0], [0, 1]], size=100)
    assert len(dist.x_arr) == 100
    assert len(dist.y_arr) == 100
    # Check if data is approximately normally distributed (basic check)
    assert dist.x_arr.mean() == pytest.approx(0, abs=0.50)
    assert dist.y_arr.mean() == pytest.approx(0, abs=0.50)
    assert dist.x_arr.std() == pytest.approx(1, abs=0.5)
    assert dist.y_arr.std() == pytest.approx(1, abs=0.5)

def test_distribution_2d_exponential():
    dist = Distribution_2D()
    dist.exponential(scale=[1, 1], size=[100, 100])
    assert len(dist.x_arr) == 100
    assert len(dist.y_arr) == 100
    # Check if data is approximately exponentially distributed (basic check)
    assert dist.x_arr.mean() == pytest.approx(1, abs=0.50)
    assert dist.y_arr.mean() == pytest.approx(1, abs=0.50)
    assert dist.x_arr.std() == pytest.approx(1, abs=0.5)
    assert dist.y_arr.std() == pytest.approx(1, abs=0.5)

def test_distribution_2d_gamma():
    dist = Distribution_2D()
    dist.gamma(shape=[1, 1], scale=[1, 1], size=[100, 100])
    assert len(dist.x_arr) == 100
    assert len(dist.y_arr) == 100
    # Check if data is approximately gamma distributed (basic check)
    assert dist.x_arr.mean() == pytest.approx(1, abs=0.50)
    assert dist.y_arr.mean() == pytest.approx(1, abs=0.50)
    assert dist.x_arr.std() == pytest.approx(1, abs=0.5)
    assert dist.y_arr.std() == pytest.approx(1, abs=0.5)