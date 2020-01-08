import Vue from 'vue'
/*********** vee-validate version 2.0.0-rc.25 **************/
import VeeValidate, { Validator } from 'vee-validate'
import zh from 'vee-validate/dist/locale/zh_CN'

Validator.addLocale(zh)

//配置
const config = {
    aria: true,
    //允许在 HTML inputs 输入框上设置 aria-invalid 和 aria-required 属性
    classNames: {},
    // 根据 input 输入框的状态应用的 class
    delay: 0,
    //所有 inputs 输入框默认的防抖时间(仅影响验证)
    locale: 'zh_CN',
    //字段(标志)对象的名称，会被注入到每个 Vue 实例的 data 里
    fieldsBagName: 'fieldBags',

}
Vue.use(VeeValidate, config)

// 自定义validate
const dictionary = {
    zh_CN: {
        /************ 错误提示语，对应v-validate，ex:请输入正确的xxxxxx **************/
        messages: {
            required: (field) => '请输入' + field,
            number: (field) => field + '必须为数值',
        },
        /************ 为空时的提示语，对应页面中的name名称，ex:请输入xxx **************/
        attributes: {
            ipAddr: 'IP地址',
            port: 'HTTP端口',
        }
    }
}
Validator.updateDictionary(dictionary)

// IPV4地址
Validator.extend('ipAddr', {
    messages: {
        zh_CN: field => '请输入正确的IPV4地址'
    },
    validate: value => {
        return /^((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))$/.test(value)
    }
})

// 端口【0~65535】
Validator.extend('port', {
    messages: {
        zh_CN: field => '请输入正确格式的端口号'
    },
    validate: value => {
        return /^([0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{4}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$/.test(value)
    }
})