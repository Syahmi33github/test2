from django import forms

from .models import PostModels

class PostForm(forms.ModelForm):
        class Meta:
                model = PostModels
                fields = [
                        'nama',
                        'cover',
                        'deskripsi',
                        'penulis',
                        'slide',
                        'sumber',
                        'category',
                        'slug',
                        'judulkatadepan',
                        'judulkatabelakang',
                        'foto1_kelipatan_150pxX200px',
                        'foto2_kelipatan_150pxX200px',
                        'foto3_kelipatan_150pxX200px',
                        'judul_latarbelakang',
                        'isi_latarbelakang',
                        'foto_latarbelakang_kelipatan_200pxX300px',
                        'judul_content1_kata_depan',
                        'judul_content1_kata_belakang',
                        'foto1_content1_kelipatan_180pxX230px',
                        'foto2_content1_kelipatan_180pxX230px',
                        'isi1_content1',
                        'isi2_content1',
                        'judul_content2_kata_depan',
                        'judul_content2_kata_belakang',
                        'fotokiri_content2_kelipatan_70pxX230px',
                        'fotokanan_content2_kelipatan_70pxX230px',
                        'isi_content2',
                        'judul_penutup_kata_depan',
                        'judul_penutup_kata_belakang',
                        'foto_penutup_kelipatan_180pxX230px',
                        'isi_penutup',
                ]