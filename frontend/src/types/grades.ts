export interface Grade {
    subject: string;
    marks: number;
}

export interface StudentGrade {
    id: string;
    cgpa: string;
    semester: number;
    created_at: string;
    updated_at: string;
    grades: Grade[]
}