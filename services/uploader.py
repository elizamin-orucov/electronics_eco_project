class Uploader:

    @staticmethod
    def product_image_uploader(instance, filename):
        return f"products/{instance.product.name}/{filename}"

    @staticmethod
    def category_uploader(instance, filename):
        return f"category/{instance.name}/{filename}"

    @staticmethod
    def brand_logo_uploader(instance, filename):
        return f"brands/{instance.brand}/{filename}"

    @staticmethod
    def blog_image_uploader(instance, filename):
        return f"blog/{instance.blog}/{filename}"


