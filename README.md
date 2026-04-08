# FarmerSchemeEnv

## Overview
AI environment to simulate farmer queries and recommend government schemes.

## Problem
Farmers lack awareness of schemes due to complex information.

## Solution
Agent learns to:
- Understand farmer queries
- Suggest correct schemes
- Explain simply

## Tasks
Easy: Basic financial help  
Medium: Crop damage  
Hard: Multi-condition query  

## Reward
Correct scheme: +1  
Wrong: -1  
Simple explanation: +0.5  
Farmer-friendly: +0.2  

## Run
docker build -t farmer-env .
docker run farmer-env

## Impact
Helps bridge gap between farmers and government schemes.
