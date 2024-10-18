import axios from 'axios';

// Set the base URL for your API
const API_URL = 'http://127.0.0.1:8000/api';  // For local development


// Helper function to get the JWT token from localStorage
const getAuthToken = () => localStorage.getItem('accessToken');

// Function for user signup
export const signup = (username, password, email) => {
  return axios.post(`${API_URL}/register/`, {
    password: password,
    email: email,
  });
};

// Function for user login
export const login = (username, password) => {
  return axios.post(`${API_URL}/token/`, {
    email: email,
    password: password,
  });
};

// Function to get user profile (protected route)
export const getUserProfile = () => {
  return axios.get(`${API_URL}/profile/`, {
    headers: {
      Authorization: `Bearer ${getAuthToken()}`,
    },
  });
};

// Function for logging out (optional, if backend supports token invalidation)
export const logout = () => {
  localStorage.removeItem('accessToken');  // Remove token from storage
};
