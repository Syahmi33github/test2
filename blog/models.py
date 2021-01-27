from django.db import models
from django.utils.text import slugify

class PostModels(models.Model):
    nama                                        = models.CharField(max_length= 30)
    deskripsi                                   = models.TextField(max_length= 255)
    cover                                       = models.ImageField(null = True, blank = True)
    penulis                                     = models.CharField(max_length= 50, default="Sam")
    slide                                       = models.CharField(max_length= 5, default="5")
    sumber                                      = models.CharField(max_length= 500, null = True, blank = True)
    category                                    = models.CharField(max_length= 50, default="Pahlawan")
    judulkatadepan                              = models.CharField(max_length= 13, default="content")
    judulkatabelakang                           = models.CharField(max_length= 13, default="content")
    foto1_kelipatan_150pxX200px                 = models.ImageField(null = True, blank = True)
    foto2_kelipatan_150pxX200px                 = models.ImageField(null = True, blank = True)
    foto3_kelipatan_150pxX200px                 = models.ImageField(null = True, blank = True)
    judul_latarbelakang                         = models.CharField(max_length= 15, default="content")
    isi_latarbelakang                           = models.TextField(max_length= 340, default="content")
    foto_latarbelakang_kelipatan_200pxX300px    = models.ImageField(null = True, blank = True)
    judul_content1_kata_depan                   = models.CharField(max_length= 23, default="content")
    judul_content1_kata_belakang                = models.CharField(max_length= 35, default="content")
    foto1_content1_kelipatan_180pxX230px        = models.ImageField(null = True, blank = True)
    foto2_content1_kelipatan_180pxX230px        = models.ImageField(null = True, blank = True)
    isi1_content1                               = models.TextField(max_length= 310, default="content")
    isi2_content1                               = models.TextField(max_length= 310, default="content")
    judul_content2_kata_depan                   = models.CharField(max_length= 15, default="content")
    judul_content2_kata_belakang                = models.CharField(max_length= 18, default="content")
    fotokiri_content2_kelipatan_70pxX230px      = models.ImageField(null = True, blank = True)
    fotokanan_content2_kelipatan_70pxX230px     = models.ImageField(null = True, blank = True)
    isi_content2                                = models.TextField(max_length= 350, default="content")
    judul_penutup_kata_depan                    = models.CharField(max_length= 18, default="content")
    judul_penutup_kata_belakang                 = models.CharField(max_length= 18, default="content")
    foto_penutup_kelipatan_180pxX230px          = models.ImageField(null = True, blank = True)
    isi_penutup                                 = models.TextField(max_length= 460, default="content")
    slug                                        = models.SlugField(blank = True)

    

    def save(self):
        self.slug = slugify(self.nama)
        super(PostModels,self).save()

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)