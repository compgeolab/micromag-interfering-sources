# Copyright (c) 2023 Gelson Ferreira de Souza-Junior, Leonardo Uieda.
# Distributed under the terms of the MIT License.
# SPDX-License-Identifier: MIT
"""
Functions for performing the processing and inversion of the microscopy data.
"""
import numpy as np



def random_unitary_vector(dispersion_angle, loc=0, size=100 ):
    """
    Creates a random unitary vector from a defined dispersion angle.

    Parameters
    ----------
    dispersion_angle: float
        Dispersion angle that defines a region in a sphere surface.
    loc:float or array_like of floats
        Mean (“centre”) of the distribution.
    size:int or tuple of ints, optional
        Output shape. If the given shape is, e.g., (m, n, k), then m * n * k 
        samples are drawn. If size is None (default), a single value is 
        returned if loc and scale are both scalars. Otherwise, 
        np.broadcast(loc, scale).size samples are drawn.

    Returns
    -------
    r_vector : :class:'numpy.ndarray' 
        A random unitary vector.
    """
    alpha = np.deg2rad(np.random.uniform(0,360,size))
    r = np.random.normal(loc, dispersion_angle, size)
    x = np.sin(r)*np.cos(alpha)
    y = np.sin(r)*np.sin(alpha)
    z = np.cos(r)

    r_vector = np.array([x,y,z])
    return r_vector

def rotate_vector(r_vector, inc, dec):
    theta = np.deg2rad(90+inc)
    phi = np.deg2rad(90-dec)

    x = r_vector[0]
    y = r_vector[1]
    z = r_vector[2]

    rotatated_vector = [
        np.cos(phi)*(x*np.cos(theta)+z*np.sin(theta))-y*np.sin(phi),
        np.sin(phi)*(x*np.cos(theta)+z*np.sin(theta))+y*np.cos(phi),
        -x*np.sin(theta)+z*np.cos(theta)
    ]
    return np.asanyarray(rotatated_vector)


def amplitude_lognormal_distribution(size, mean=0, dev_pad=1.5, seed=None):
    """
    Generates amplitude values in a lognormal distribution
    """
    np.random.seed(seed)
    lognormal_distribution = np.random.lognormal(mean, dev_pad, size)
    return lognormal_distribution * 1E-14