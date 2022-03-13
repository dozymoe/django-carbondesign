import m from 'mithril/hyperscript';
//-
import { Node, modify_svg } from './base';

export class Grid extends Node
{
    WANT_CHILDREN = true
    MODES = ['default', 'bleed']
    NODE_PROPS = ['full_width', 'gap']
    GAP_SIZES = ['narrow', 'condensed']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.full_width)
        {
            values['class'].push('bx--grid--full-width');
        }

        let gap = vnode.attrs.gap;
        if (gap)
        {
            values['class'].push(`bx--grid--${gap}`);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--grid ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_bleed(vnode, values, context)
    {
        return (
//##
m('div.bleed', null,
  m(values.tag,
    {
      'class': `bx--grid ${values['class']}`,
      ...values.props,
    },
    values.child))
//##
        );
    }
}


export class Row extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--row ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class Col extends Node
{
    WANT_CHILDREN = true
    COL_SIZES = ['sm', 'md', 'lg', 'xlg', 'max']
    NODE_PROPS = COL_SIZES + COL_SIZES.map(x => `offset_${x}`)

    prepare(vnode, values, context)
    {
        for (let size of this.COL_SIZES)
        {
            let width = vnode.attrs[size]
            if (width)
            {
                this.has_size = true;
                values['class'].push(`bx--col-${size}-${width}`);
            }

            width = vnode.attrs[`offset-${size}`];
            if (width)
            {
                values['class'].push(`bx--offset-${size}-${width}`);
            }
        }
        if (!this.has_size)
        {
            values['class'].push('bx--col');
            values['class'].push('bx--col--auto');
        }
    }

    render_default(vnode, values, context)
    {
        if (this.has_size)
        {
            return (
//##
m(values.tag,
  {
    'class': values['class'],
    ...values.props,
  },
  m('div.outside', null,
    m('div.inside', null, values.child)))
//##
            );
        }

        return (
//##
m(values.tag, {'class': values['class'], ...values.props}, values.child)
//##
        );
    }
}


export class AspectRatio extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['ratio']

    prepare(vnode, values, context)
    {
        let ratio = vnode.attrs.ratio;
        if (ratio)
        {
            values['class'].push(`bx--aspect-ratio--${ratio}`);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--aspect-ratio ${values['class']}`,
    ...values.props,
  },
  m('div.bx--aspect-ratio--object', null, values.child))
//##
        );
    }
}
