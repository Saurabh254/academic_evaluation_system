
import apiClient from "@/common/base_api"

export const FetchStudentList = async () => {
    return await apiClient.get('/students/all')
}

