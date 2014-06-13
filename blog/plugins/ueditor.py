#coding:utf-8
import xadmin
from django.db.models import TextField
from xadmin import widgets
from xadmin.views import BaseAdminPlugin, ModelFormAdminView, DetailAdminView
from DjangoUeditor.widgets import UEditorWidget 
from DjangoUeditor.utils import MadeUeditorOptions
from django.utils.html import  conditional_escape
from django.utils.encoding import  force_unicode

class UeditorPlugin(BaseAdminPlugin):
    ueditor_options = {}
    def init_request(self, *args, **kwargs):
        print '8'*40
        print self.ueditor_options
        self.model
        print args
        print kwargs
        print self.ueditor_options
        print bool(self.ueditor_options)
        return bool(self.ueditor_options)

    def get_field_result(self, result, field_name):
        print '9'*40
        if self.admin_view.style_fields.get(field_name) in ('ueditor-mini', 'ueditor-normal', 'ueditor-full'):
            result.allow_tags = True
        return result

    # Media
    def get_media(self, media):
        print 'get_media'
        css={"all": ("ueditor/themes/default/css/ueditor.css" ,
                     "ueditor/themes/iframe.css" ,
            )}
        js=("ueditor/editor_config.js",
            "ueditor/editor_all_min.js")
        media.css = css
        media.add_js([self.static("ueditor/editor_config.js"),self.static("ueditor/editor_all_min.js"),])
        return media

    #def block_top_toolbar__(self, context, nodes):
    def render_response(content, response_type='json'):
        print 'block_content'
        #current_refresh = self.request.GET.get(REFRESH_VAR)
        #context.update({
        #    'has_refresh': bool(current_refresh),
        #    'clean_refresh_url': self.admin_view.get_query_string(remove=(REFRESH_VAR,)),
        #    'current_refresh': current_refresh,
        #    'refresh_times': [{
        #        'time': r,
        #        'url': self.admin_view.get_query_string({REFRESH_VAR: r}),
        #        'selected': str(r) == current_refresh,
        #    } for r in self.refresh_times],
        #})
        ## 可以将 HTML 片段加入 nodes 参数中
        #nodes.append(loader.render_to_string('xadmin/blocks/refresh.html', context_instance=context))




        #if value is None: value = ''
        ##取得工具栏设置
        print '+'*40
        print context
        print nodes
        try:
            if type(self.ueditor_options['toolbars'])==list:
                tbar=simplejson.dumps(self.ueditor_options['toolbars'])
            else:
                if getattr(USettings,"TOOLBARS_SETTINGS",{}).has_key(str(self.ueditor_options['toolbars'])):
                    if self.ueditor_options['toolbars'] =="full":
                        tbar=None
                    else:
                        tbar=simplejson.dumps(USettings.TOOLBARS_SETTINGS[str(self.ueditor_options['toolbars'])])
                else:
                    tbar=None
        except:
            pass

        #传入模板的参数
        uOptions=self.ueditor_options.copy()
        uOptions.update({
            "name":'name',
            "value":conditional_escape(force_unicode(value)),
            "toolbars":tbar,
            "options":simplejson.dumps(self.ueditor_options['options'])[1:-1]
                #str(self.ueditor_options['options'])[1:-1].replace("True","true").replace("False","false").replace("'",'"')
        })
        context = {
                'UEditor':uOptions,
                'STATIC_URL':settings.STATIC_URL,
                'STATIC_ROOT':settings.STATIC_ROOT,
                'MEDIA_URL':settings.MEDIA_URL,
                'MEDIA_ROOT':settings.MEDIA_ROOT
        }
        print 'T'*40
        print nodes.append(loader.render_to_string('ueditor.html', context_instance=context))
        return nodes.append(loader.render_to_string('ueditor.html', context_instance=context))
        #return mark_safe(render_to_string('ueditor.html',context))

xadmin.site.register_plugin(UeditorPlugin, DetailAdminView)
xadmin.site.register_plugin(UeditorPlugin, ModelFormAdminView)
