class SD3ClipSwap:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "sd3_clip": ("CLIP",),
                              "sdxl_clip": ("CLIP",),
                              }}
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "modify"

    CATEGORY = "advanced/clip_hacks"

    def modify(self, sd3_clip, sdxl_clip):
        modified_sd3_clip = sd3_clip.clone()
        modified_sd3_clip.cond_stage_model.clip_l = sdxl_clip.cond_stage_model.clip_l
        modified_sd3_clip.cond_stage_model.clip_g = sdxl_clip.cond_stage_model.clip_g
        return (modified_sd3_clip, )

NODE_CLASS_MAPPINGS = {
    "SD3ClipSwap": SD3ClipSwap,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SD3ClipSwap": "SD3 Clip Swap",
}