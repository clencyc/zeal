export const saveToken = (token) => {
    localStorage.setItem('accessToken', token);
  };
  
  export const getToken = () => {
    return localStorage.getItem('accessToken');
  };

  