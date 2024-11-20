import axios, { AxiosInstance, AxiosResponse, AxiosError } from "axios";

const getToken = (): string | null => localStorage.getItem("access_token");

export interface ApiResponse<T> {
  success: boolean;
  data: T;
  message?: string;
}

const apiClient: AxiosInstance = axios.create({
  baseURL: "http://localhost:8000/api/v1",
  timeout: 10000,
});
export const apiClientNoAuth: AxiosInstance = axios.create({
  baseURL: "http://localhost:8000/api/v1",
  timeout: 10000,
});
apiClientNoAuth.interceptors.request.use(config => {
  config.baseURL = "http://localhost:8000/api/v1";  // Make sure this is correctly set.
  return config;
});


apiClient.interceptors.request.use(
  (request) => {
    const accessToken = getToken();
    if (accessToken) {
      request.headers["Authorization"] = `Bearer ${accessToken}`;
    }
    return request;
  },
  (error) => {
    return Promise.reject(error);
  },
);

apiClient.interceptors.response.use(
  (response: AxiosResponse): AxiosResponse => response,
  (error: AxiosError): Promise<AxiosError> => {
    if (error.response?.status === 401) {
      localStorage.removeItem("access_token");
      window.location.href = "/login";
    }
    return Promise.reject(error);
  },
);

export default apiClient;
