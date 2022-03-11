import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class ProgressIndicator extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['vertical']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.vertical)
        {
            values['class'].push('bx--progress--vertical');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('ul',
  {
    'data-progress': '',
    'data-progress-current': '',
    'class': `bx--progress ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class ProgressIndicatorItem extends Node
{
    SLOTS = ['optional']
    NODE_PROPS = ['variant']

    prepare(vnode, values, context)
    {
        let variant = this.variant = vnode.attrs.variant;
        values['class'].push(`bx--progress-step--${variant}`);

        if (variant === 'invalid')
        {
            values.props.push(['data-invalid', '']);
        }
        else if (variant === 'disabled')
        {
            values['class'].push('bx--progress-step--incomplete');
            values.props.push(['aria-disabled', 'true']);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('li',
  {
    'class': `bx--progress-step ${values['class']}`,
    ...values.props,
  },
  [
    m('svg', null,
      m('path',
        {
          d: 'M 7, 7 m -7, 0 a 7,7 0 1,0 14,0 a 7,7 0 1,0 -14,0',
        })),
    m('p',
      {
        tabindex: 0,
        'class': `bx--progress-label ${values.label_class}`,
        'aria-describedby': values.id,
        ...values.label_props,
      },
      values.label),
    m('div',
      {
        id: values.id,
        role: 'tooltip',
        'data-floating-menu-direction': 'bottom',
        'class': 'bx--tooltip',
        'data-avoid-focus-on-open': '',
      },
      [
        m('span.bx--tooltip__caret'),
        m('p.bx--tooltip__text', null, values.child),
      ]),
    this.slot('optional', vnode, values, context),
    m('span.bx--progress-line'),
  ])
//##
        );
    }

    render_slot_optional(vnode, values, context)
    {
        return (
//##
m('p',
  {
    'class': `bx--progress-optional ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_tmpl_icon(vnode, values, context)
    {
        if (this.variant === 'current')
        {
            return (
//##
m('svg', null,
  m('path',
    {
      d: 'M 7, 7 m -7, 0 a 7,7 0 1,0 14,0 a 7,7 0 1,0 -14,0',
    }))
//##
            );
        }
        if (this.variant === 'complete')
        {
            return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'currentColor',
    width: 16,
    height: 16,
    viewBox: '0 0 32 32',
    'aria-hidden': true,
  },
  [
    m('path',
      {
        d: 'M14 21.414L9 16.413 10.413 15 14 18.586 21.585 11 23 12.415 14 \
            21.414z',
      }),
    m('path',
      {
        d: 'M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,26A12,12,0,1,1,28,16,\
            12,12,0,0,1,16,28Z',
      }),
  ])
//##
            );
        }
        if (this.variant === 'incomplete')
        {
            return (
//##
m('svg', null,
  m('path',
    {
      d: 'M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 \
          0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z',
    }))
//##
            );
        }
        if (this.variant === 'invalid')
        {
            return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'currentColor',
    'class': 'bx--progress__warning',
    width: 16,
    height: 16,
    viewBox: '0 0 16 16',
    'aria-hidden': true,
  },
  [
    m('path',
      {
        d: 'M8,1C4.1,1,1,4.1,1,8s3.1,7,7,7s7-3.1,7-7S11.9,1,8,1z M8,14c-3.3,\
            0-6-2.7-6-6s2.7-6,6-6s6,2.7,6,6S11.3,14,8,14z',
      }),
    m('path',
      {
        d: 'M7.5 4H8.5V9H7.5zM8 10.2c-.4 0-.8.3-.8.8s.3.8.8.8c.4 0 .8-.3.8-.\
            8S8.4 10.2 8 10.2z',
      }),
  ])
//##
            );
        }
        if (this.variant === 'disabled')
        {
            return (
//##
m('svg', null,
  m('path',
    {
      d: 'M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 0-6-2.\
          7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z',
    }))
//##
            );
        }
        return '';
    }
}
