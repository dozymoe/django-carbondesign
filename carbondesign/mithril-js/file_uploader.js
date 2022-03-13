import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';

export class File extends FormNode
{
    prepare(vnode, values, context)
    {
        values.txt_drop = gettext("Drag and drop files here or upload");
        values.txt_clear = gettext("Remove uploaded file");
    }

    prepare_element_props(vnode, props, default_props, context)
    {
        props['class'].push('bx--file-input');
        props['data-file-uploader'] = '';
        props['data-target'] = `#container-${this.id(context)}`
    }

    render_default(vnode, values, context)
    {
        let filename = this.bound_field.value();

        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  [
    m('strong',
      {
        'class': `bx--file--label ${values.label_class}`,
        ...values.label_props,
      },
      values.label),
    this.tmpl('help', vnode, values, context),
    m('div.bx--file',
      {
        'data-file': '',
      },
      [
        m('label',
          {
            'for': values.id,
            'class': 'bx--file-browse-btn',
            role: 'button',
            tabindex: 0,
          },
          m('div',
            {
              'data-file-drop-container': '',
              'class': 'bx--file__drop-container',
            },
            [
              values.txt_drop,
              values.element,
            ])),
        m('div',
          {
            'data-file-container': '',
            id: `container-${values.id}`,
            'class': 'bx--file-container',
          },
          m('div.bx--file__selected-file.bx--file__selected-file--invalid',
            {
              'data-invalid': '',
            },
            [
              m('p.bx--file-filename', null, filename),
              m('span',
                {
                  'data-for': 'prepopulated-file-uploader',
                  'class': 'bx--file__state-container',
                },
                m('svg',
                  {
                    focusable: false,
                    preserveAspectRatio: 'xMidYMid meet',
                    xmlns: 'http://www.w3.org/2000/svg',
                    fill: 'currentColor',
                    'class': 'bx--file--invalid',
                    width: 16,
                    height: 16,
                    viewBox: '0 0 16 16',
                    'aria-hidden': true,
                  },
                  [
                    m('path',
                      {
                        d: 'M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,\
                            8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2  \
                            c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,\
                            0.4,0.8,0.8S8.4,12.2,8,12.2z',
                      }),
                    m('path',
                      {
                        d: 'M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,\
                            0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,\
                            0.8,0.8S8.4,12.2,8,12.2z',
                        'data-icon-path': 'inner-path',
                        opacity: 0,
                      }),
                  ]),
                m('svg',
                  {
                    focusable: true,
                    preserveAspectRatio: 'xMidYMid meet',
                    xmlns: 'http://www.w3.org/2000/svg',
                    fill: 'currentColor',
                    'aria-label': values.txt_clear,
                    'class': 'bx--file-close',
                    width: 16,
                    height: 16,
                    viewBox: '0 0 32 32',
                    role: 'img',
                    tabindex: 0,
                  },
                  m('path',
                    {
                      d: 'M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 \
                          9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z',
                    }))),
              m('div.bx--form-requirement', null, values.form_errors),
            ])),
      ]),
  ])
//##
            );
        }

        if (filename)
        {
            return (
//##
m('div.bx--form-item', null,
  [
    m('strong',
      {
        'class': `bx--file--label ${values.label_class}`,
        ...values.label_props,
      },
      values.label),
    this.tmpl('help', vnode, values, context),
    m('div.bx--file',
      {
        'data-file': '',
      },
      [
        m('label',
          {
            'for': values.id,
            'class': 'bx--file-browse-btn',
            role: 'button',
            tabindex: 0,
          },
          m('div',
            {
              'data-file-drop-container': '',
              'class': 'bx--file__drop-container',
            },
            [
              values.txt_drop,
              values.element,
            ])),
        m('div',
          {
            'data-file-container': '',
            id: `container-${values.id}`,
            'class': 'bx--file-container',
          },
          m('div.bx--file__selected-file', null,
            [
              m('p.bx--file-filename', null, filename),
              m('span',
                {
                  'data-for': 'prepopulated-file-uploader',
                  'class': 'bx--file__state-container',
                },
                m('svg',
                  {
                    focusable: false,
                    preserveAspectRatio: 'xMidYMid meet',
                    xmlns: 'http://www.w3.org/2000/svg',
                    fill: 'currentColor',
                    'class': 'bx--file--invalid',
                    width: 16,
                    height: 16,
                    viewBox: '0 0 16 16',
                    'aria-hidden': true,
                  },
                  [
                    m('path',
                      {
                        d: 'M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,\
                            8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2  \
                            c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,\
                            0.4,0.8,0.8S8.4,12.2,8,12.2z',
                      }),
                    m('path',
                      {
                        d: 'M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,\
                            0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,\
                            0.8,0.8S8.4,12.2,8,12.2z',
                        'data-icon-path': 'inner-path',
                        opacity: 0,
                      }),
                  ])),
            ])),
      ]),
  ])
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  [
    m('strong',
      {
        'class': `bx--file--label ${values.label_class}`,
        ...values.label_props,
      },
      values.label),
    this.tmpl('help', vnode, values, context),
    m('div.bx--file',
      {
        'data-file': '',
      },
      [
        m('label',
          {
            'for': values.id,
            'class': 'bx--file-browse-btn',
            role: 'button',
            tabindex: 0,
          },
          m('div',
            {
              'data-file-drop-container': '',
              'class': 'bx--file__drop-container',
            },
            [
              values.txt_drop,
              values.element,
            ])),
        m('div',
          {
            'data-file-container': '',
            id: `container-${values.id}`,
            'class': 'bx--file-container',
          }),
      ]),
  ])
//##
        );
    }

    render_tmpl_help(vnode, values, context)
    {
        if (this.bound_field.help_text)
        {
            return (
//##
m('p',
  {
    'class': `bx--label-description ${values.help_class}`,
    ...values.help_props,
  },
  this.bound_field.help_text)
//##
            );
        }
    }
}
