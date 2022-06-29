import m from 'mithril/hyperscript';
//-
import messages from './messages.json';
import { Node } from './base';

export class Notification extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['action']
    MODES = ['inline', 'toast']
    NODE_PROPS = ['variant', 'low_contrast']

    prepare(vnode, values, context)
    {
        values.txt_close = gettext("close");

        let variant = this.variant = vnode.attrs.variant || 'info';
        if (variant === messages.DEBUG || variant === messages.INFO)
        {
            this.variant = 'info';
        }
        else if (variant === messages.SUCCESS)
        {
            this.variant = 'success';
        }
        else if (variant === messages.WARNING)
        {
            this.variant = 'warning';
        }
        else if (varaint === messages.ERROR)
        {
            this.variant = 'error';
        }

        values['class'].push(`bx--${this.mode}-notification--${variant}`);

        if (vnode.attrs.low_contrast)
        {
            values['class'].push(`bx--${this.mode}-notification--low-contrast`);
        }

        context.mode = this.mode;
    }

    render_inline(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'data-notification': '',
    'class': `bx--inline-notification ${values['class']}`,
    role: 'alert',
  },
  [
    m('div.bx--inline-notification__details', null,
      [
        this.tmpl('icon', vnode, values, context),
        m('div.bx--inline-notification__text-wrapper', null, values.child),
      ]),
    this.slot('action', vnode, values, context),
    this.tmpl('close', vnode, values, context),
  ])
//##
        );
    }

    render_toast(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'data-notification': '',
    'class': `bx--toast-notification ${values['class']}`,
    role: 'alert',
  },
  [
    this.tmpl('icon', vnode, values, context),
    m('div.bx--toast-notification__details', null, values.child),
    this.tmpl('close', vnode, values, context),
  ])
//##
        );
    }

    render_tmpl_icon(vnode, values, context)
    {
        if (this.variant === 'info')
        {
            return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'currentColor',
    'class': `bx--${this.mode}-notification__icon`,
    width: 20,
    height: 20,
    viewBox: '0 0 32 32',
    'aria-hidden': true,
  },
  [
    m('path',
      {
        fill: 'none',
        d: 'M16,8a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,13.875H17.\
            125v-8H13v2.25h1.875v5.75H12v2.25h8Z',
        'data-icon-path': 'inner-path',
      }),
    m('path',
      {
        d: 'M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,6a1.5,1.5,0,1,1-1.5,\
            1.5A1.5,1.5,0,0,1,16,8Zm4,16.125H12v-2.25h2.875v-5.75H13v-2.25h4.\
            125v8H20Z',
      }),
  ])
//##
            );
        }

        if (this.variant === 'error')
        {
            return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'currentColor',
    'class': `bx--${this.mode}-notification__icon`,
    width: 20,
    height: 20,
    viewBox: '0 0 20 20',
    'aria-hidden': true,
  },
  [
    m('path',
      {
        d: 'M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M13.5,14.5l-8-8l1-\
            1l8,8L13.5,14.5z',
      }),
    m('path',
      {
        d: 'M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z',
        'data-icon-path': 'inner-path',
        opacity: 0,
      }),
  ])
//##
            );
        }

        if (this.variant === 'success')
        {
            return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'currentColor',
    'class': `bx--${this.mode}-notification__icon`,
    width: 20,
    height: 20,
    viewBox: '0 0 20 20',
    'aria-hidden': true,
  },
  [
    m('path',
      {
        d: 'M10,1c-4.9,0-9,4.1-9,9s4.1,9,9,9s9-4,9-9S15,1,10,1z M8.7,13.5l-\
            3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z',
      }),
    m('path',
      {
        fill: 'none',
        d: 'M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z',
        'data-icon-path': 'inner-path',
        opacity: 0,
      }),
  ])
//##
            );
        }

        if (this.variant === 'warning')
        {
            return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'currentColor',
    'class': `bx--${this.mode}-notification__icon`,
    width: 20,
    height: 20,
    viewBox: '0 0 20 20',
    'aria-hidden': true,
  },
  [
    m('path',
      {
        d: 'M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M9.2,5h1.5v7H9.2V5z \
            M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1  s1,0.4,1,1S10.6,16,10,16z',
      }),
    m('path',
      {
        d: 'M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1s1,0.4,1,\
            1S10.6,16,10,16z',
        'data-icon-path': 'inner-path',
        opacity: 0,
      }),
  ])
//##
            );
        }
    }

    render_tmpl_close(vnode, values, context)
    {
        return (
//##
m('button',
  {
    'data-notification-btn': '',
    'class': `bx--${this.mode}-notification__close-button`,
    type: 'button',
    'aria-label': values.txt_close,
  },
  m('svg',
    {
      focusable: false,
      preserveAspectRatio: 'xMidYMid meet',
      xmlns: 'http://www.w3.org/2000/svg',
      fill: 'currentColor',
      'class': `bx--${this.mode}-notification__close-icon`,
      width: 20,
      height: 20,
      viewBox: '0 0 32 32',
      'aria-hidden': true,
    },
    m('path',
      {
        d: 'M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 \
            22.6 24 24 22.6 17.4 16 24 9.4z',
      })))
//##
        );
    }
}

export class NotificationButton extends Node
{
    WANT_CHILDREN = true
    DEFAULT_TAG = 'button'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.astag,
  {
    tabindex: 0,
    'class': `bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}

export class NotificationTitle extends Node
{
    WANT_CHILDREN = true
    DEFAULT_TAG = 'h3'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.astag,
  {
    'class': `bx--${context.mode}-notification__title ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}

export class NotificationSubtitle extends Node
{
    WANT_CHILDREN = true
    DEFAULT_TAG = 'p'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.astag,
  {
    'class': `bx--${context.mode}-notification__subtitle ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}

export class NotificationCaption extends Node
{
    WANT_CHILDREN = true
    DEFAULT_TAG = 'p'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.astag,
  {
    'class': `bx--${context.mode}-notification__caption ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}
