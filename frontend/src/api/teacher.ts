import apiClient from "@/common/base_api"

export const FetchTeacher = async () => {
    return await apiClient.get('/teachers/me')
}
