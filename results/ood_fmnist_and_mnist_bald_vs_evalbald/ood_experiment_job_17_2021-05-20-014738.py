store = {}
store['timestamp']=1621471658
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=17']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=17
store['worker_id']=17
store['num_workers']=80
store['config']={'seed': 1252, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.472931385040283})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.171750545501709})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.116522789001465})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.3821253776550293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.436509132385254})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.4035284519195557})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6081, 'crossentropy': 3.24521640625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.773141860961914})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.7168614864349365})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.7485651969909668})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.6615321636199951})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.757546067237854})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 50752], ['id', 8583], ['id', 28342], ['id', 7756], ['id', 37318]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0709581874002105, 1.875381511276733, 2.3856661911812047, 2.725292551733741, 2.9045486388566775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.0114779472351074})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.0610201358795166})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.393038511276245})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.254940986633301})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5814, 'crossentropy': 2.0229265625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3716148138046265})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.333451509475708})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.300484538078308})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 1058], ['id', 25144], ['id', 13428], ['id', 47545], ['id', 34940]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4438594627252521, 0.7833193621167647, 1.0895612079048265, 1.3078127896953875, 1.4731209444539006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.8510290384292603})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.307793378829956})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.544424533843994})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.922159194946289})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.790600538253784})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.9445691108703613})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.9740781784057617})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.0522565841674805})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.076205253601074})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.0721189975738525})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5731, 'crossentropy': 3.280050390625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.5938868522644043})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.7673263549804688})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.8187119960784912})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.64628005027771})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.7649040222167969})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 50221], ['id', 48964], ['id', 41348], ['id', 50604], ['id', 23053]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7522501827898316, 1.3657975539979046, 1.8515654779287907, 2.2049592148381496, 2.4654975924251694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.4540170431137085})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 2.0500786304473877})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.190725326538086})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.64640212059021})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.9858062267303467})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.8178393840789795})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.93448543548584})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.8040883541107178})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.9643304347991943})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.0618019104003906})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.1245665550231934})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.152353286743164})
store['active_learning_steps'][3]['training']['best_epoch']=9
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5877, 'crossentropy': 2.99400625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.5123854875564575})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.507002830505371})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.7527265548706055})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.5903517007827759})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.7505898475646973})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.6838139295578003})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 31398], ['id', 40363], ['id', 50938], ['id', 13883], ['id', 39750]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7640451352114295, 1.4475680382386298, 1.9983035349014386, 2.395592673307739, 2.697976801336306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.4492019414901733})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.8777961730957031})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.323868751525879})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.481269359588623})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.374290943145752})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5954, 'crossentropy': 1.9655390625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.330296277999878})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.317901372909546})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.306885004043579})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2826993465423584})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 47864], ['id', 12746], ['id', 40979], ['id', 19842], ['id', 15911]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6338559487359108, 1.1453117717466248, 1.6040612688982065, 1.9163813837119301, 2.1744738184039853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.36710524559021})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.8387441635131836})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.0585711002349854})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.389404296875})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.349036455154419})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.5337867736816406})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6105, 'crossentropy': 2.1089814453125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2653589248657227})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3643525838851929})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4217803478240967})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4031867980957031})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.321002721786499})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 52503], ['id', 58451], ['id', 55475], ['id', 55837], ['id', 52926]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5720570936629215, 1.0721658844863207, 1.5087458279278403, 1.8547883704624795, 2.096794915815485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.326404094696045})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.5863145589828491})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.97027587890625})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.055039882659912})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.1759424209594727})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6344, 'crossentropy': 1.6906892578125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.215419054031372})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2112798690795898})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2276607751846313})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1503371000289917})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 31612], ['id', 4752], ['id', 50827], ['id', 6000], ['id', 10468]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.674463231288063, 1.1257484243926617, 1.5176098137253184, 1.835317657492073, 2.0751486358453306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3090777397155762})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.644268274307251})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9156287908554077})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.0879569053649902})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.22662353515625})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.4888439178466797})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.284247398376465})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7365245819091797})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.165687084197998})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.6102681159973145})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.7324271202087402})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6589736938476562})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.872952461242676})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7819159030914307})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.8815107345581055})
store['active_learning_steps'][7]['training']['best_epoch']=12
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6357, 'crossentropy': 2.8535142578125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2114571332931519})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3445727825164795})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3202910423278809})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4218840599060059})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.4251439571380615})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5272600650787354})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.304198980331421})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4476025104522705})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4115921258926392})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.385998249053955})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4067351818084717})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3943769931793213})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3326624631881714})
store['active_learning_steps'][7]['eval_training']['best_epoch']=10
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 44208], ['id', 57751], ['id', 23344], ['id', 16996], ['id', 10010]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8872008943269531, 1.513329300146897, 2.024580645607486, 2.4187805283800055, 2.700489310620517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3835088014602661})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.7414097785949707})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.7384555339813232})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.8759877681732178})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.0359151363372803})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.1975791454315186})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.197061061859131})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.285252809524536})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.463338851928711})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.2472896575927734})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.411247730255127})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.477480411529541})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.252387285232544})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.29140567779541})
store['active_learning_steps'][8]['training']['best_epoch']=11
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6325, 'crossentropy': 2.457261328125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2783927917480469})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2545783519744873})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4232875108718872})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4006896018981934})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4027369022369385})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4051809310913086})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3434109687805176})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4292608499526978})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 3194], ['id', 5937], ['id', 40453], ['id', 36274], ['id', 24734]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7268973057817627, 1.3752920967633575, 1.84175735794342, 2.1980434986491373, 2.4293611081553186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.312582015991211})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4868686199188232})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.6920949220657349})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.9087042808532715})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.9478795528411865})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.1872267723083496})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.648, 'crossentropy': 1.6684263671875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.2641520500183105})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1852045059204102})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1873188018798828})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1673054695129395})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.174208402633667})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 53467], ['id', 40721], ['id', 54835], ['id', 27077], ['id', 6984]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49640899405720496, 0.9502061284270411, 1.3186605749582085, 1.6208833004998402, 1.8416896883527833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.3778114318847656})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4010491371154785})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6543669700622559})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.8233873844146729})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.6534738540649414})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8966352939605713})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6571, 'crossentropy': 1.7146322265625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2613372802734375})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2608134746551514})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1301268339157104})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1595382690429688})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1326524019241333})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 42587], ['id', 33533], ['id', 3225], ['id', 59703], ['id', 39489]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4922265806173476, 0.9368660191483311, 1.296616730023909, 1.6132469376901488, 1.853616652892235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.3751013278961182})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3638941049575806})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.6308140754699707})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.7152411937713623})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.8990323543548584})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.8142402172088623})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.0210533142089844})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6663, 'crossentropy': 1.7278416015625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.2684577703475952})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.158096194267273})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1480151414871216})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1247379779815674})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1043007373809814})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.090261459350586})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 38618], ['id', 17267], ['id', 59771], ['id', 47704], ['id', 26978]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5666009229641686, 1.101056972248931, 1.5138032204885938, 1.8233757366989458, 2.0619799908600527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.3916099071502686})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2268595695495605})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4295251369476318})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.6420879364013672})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.7525606155395508})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.8252880573272705})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.1903247833251953})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6792, 'crossentropy': 1.731430078125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2348201274871826})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1254041194915771})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.110285758972168})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1015129089355469})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1124682426452637})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1064343452453613})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 54187], ['id', 35111], ['id', 32349], ['id', 56948], ['id', 51769]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6176833216737156, 1.1079579505817834, 1.5254100315393604, 1.8475688167739062, 2.0573434291226604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.346754550933838})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.227766752243042})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.4994874000549316})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.6912603378295898})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.6224608421325684})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.0639655590057373})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.29240083694458})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.083252429962158})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.227184772491455})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.085986852645874})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.689744472503662})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6932, 'crossentropy': 2.031058984375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2674016952514648})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1527996063232422})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2221271991729736})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.274474859237671})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1857057809829712})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3208630084991455})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2978888750076294})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 1254], ['id', 7683], ['id', 59091], ['id', 52114], ['id', 11921]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6291135442204634, 1.1930254808029455, 1.577438739985301, 1.8752299630620817, 2.096834931818737]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.296720027923584})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2309261560440063})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.5157431364059448})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.5970996618270874})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.6687989234924316})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8618288040161133})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.9208095073699951})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.9879072904586792})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.993347406387329})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.06074857711792})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.3164892196655273})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7077, 'crossentropy': 1.8524455078125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1574903726577759})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1423332691192627})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2663941383361816})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.4123191833496094})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.261832356452942})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2624326944351196})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2349393367767334})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2551460266113281})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1964609622955322})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 900], ['id', 19330], ['id', 57177], ['id', 20550], ['id', 24851]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6350950910739195, 1.1852261972365934, 1.6493531063781113, 1.9938494114679841, 2.2463164888171168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3129124641418457})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1239535808563232})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4583659172058105})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4887568950653076})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5799517631530762})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6822572946548462})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.69663667678833})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.962465763092041})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.8610148429870605})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.8814818859100342})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.2413883209228516})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.0633320808410645})
store['active_learning_steps'][15]['training']['best_epoch']=9
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7154, 'crossentropy': 1.8466294921875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1744821071624756})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1686935424804688})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2284448146820068})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.3393832445144653})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3156049251556396})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.2341960668563843})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3267297744750977})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.341749906539917})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3356561660766602})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 5692], ['id', 14065], ['id', 51767], ['id', 3853], ['id', 58689]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6612578439363612, 1.184575078546561, 1.6408808738529457, 1.9767280475512816, 2.200865465775334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.254263162612915})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1736706495285034})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3255856037139893})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.6511051654815674})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.6851222515106201})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.9795929193496704})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6868, 'crossentropy': 1.36891044921875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2194750308990479})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1079182624816895})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0609915256500244})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0498032569885254})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0276329517364502})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 47659], ['id', 24079], ['id', 47513], ['id', 56746], ['id', 42361]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6038963612116564, 1.130457835325715, 1.5544704373922382, 1.8827033125634234, 2.1244816961923885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2174134254455566})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.184880256652832})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.257657527923584})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.6227474212646484})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8216040134429932})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6876, 'crossentropy': 1.17185185546875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1668140888214111})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0238147974014282})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0080453157424927})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9870026111602783})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 28663], ['id', 57213], ['id', 55367], ['id', 43510], ['id', 36552]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.499018336270459, 0.8869904761054119, 1.2187119033899645, 1.5168519415157116, 1.7569986285349302]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.3055098056793213})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1839447021484375})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2220299243927002})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.4817092418670654})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5539484024047852})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.7169597148895264})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.6156339645385742})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.103025197982788})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.2140097618103027})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6961, 'crossentropy': 1.8927935546875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1996647119522095})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0537114143371582})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1413096189498901})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1788190603256226})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.091935157775879})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1253535747528076})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1054257154464722})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0717873573303223})
store['active_learning_steps'][18]['eval_training']['best_epoch']=8
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 27863], ['id', 18126], ['id', 56233], ['id', 30902], ['id', 39809]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6269964955644984, 1.2161678166616068, 1.6888041673238678, 2.0447749182812682, 2.286228980650046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3426775932312012})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1489067077636719})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3156466484069824})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3828461170196533})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.8164782524108887})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.6913090944290161})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.8493664264678955})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.1715831756591797})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8862195014953613})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.0904951095581055})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.063098669052124})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.2673048973083496})
store['active_learning_steps'][19]['training']['best_epoch']=9
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6901, 'crossentropy': 2.007353125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.172966718673706})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.124008059501648})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.168036699295044})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.133465051651001})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.161545753479004})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1585289239883423})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1996670961380005})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 8763], ['id', 41044], ['id', 58772], ['id', 50989], ['id', 39707]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6351966677704477, 1.1939022541001298, 1.633924237821879, 1.9545108304164565, 2.170221743189707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.410491943359375})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.108377456665039})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.2276947498321533})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3585712909698486})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4884867668151855})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.444772720336914})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7072, 'crossentropy': 1.25560302734375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2229151725769043})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.056087851524353})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0149331092834473})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.006996750831604})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0222182273864746})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 50385], ['id', 56380], ['id', 56900], ['id', 34122], ['id', 7595]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5277576400852126, 0.9495825733707277, 1.3272500568900023, 1.6255391913425568, 1.8743755059991507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3583990335464478})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0960338115692139})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.282225251197815})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.5052305459976196})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5599888563156128})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6749, 'crossentropy': 1.13821708984375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2306036949157715})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.098219871520996})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.05001699924469})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0745201110839844})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 10259], ['id', 56027], ['id', 41355], ['id', 28733], ['id', 10785]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.44725273874169713, 0.8538003203668816, 1.209003453831941, 1.5336257566927554, 1.797443090943025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.4150340557098389})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0865111351013184})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1014351844787598})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4223663806915283})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.4599592685699463})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.4983720779418945})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.6170539855957031})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.7133359909057617})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.8413424491882324})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9228272438049316})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.754272699356079})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.8035483360290527})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.8602845668792725})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.9249029159545898})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.836092233657837})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.9783380031585693})
store['active_learning_steps'][22]['training']['best_epoch']=13
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7144, 'crossentropy': 1.7676708984375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.2915397882461548})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0541927814483643})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.1147582530975342})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1559655666351318})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.114334225654602})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2311890125274658})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 22970], ['id', 9658], ['id', 37389], ['id', 43735], ['id', 56246]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6835925279027864, 1.270832888015586, 1.7041946893565947, 2.0653904264413434, 2.331352623697663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.3989793062210083})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1585487127304077})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2736659049987793})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2334532737731934})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.3435028791427612})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.5235583782196045})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.6194459199905396})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.6562602519989014})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.8138761520385742})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.9079279899597168})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.8617784976959229})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.717, 'crossentropy': 1.56943515625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.365160346031189})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0662908554077148})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0605103969573975})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0279102325439453})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0747199058532715})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.041046142578125})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0441834926605225})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0004695653915405})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 28940], ['id', 20867], ['id', 26663], ['id', 33141], ['id', 10226]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5515740607495889, 1.0141387950054486, 1.4288949672493265, 1.7475029835088929, 1.9524186791307887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.4096007347106934})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1493232250213623})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2542774677276611})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3037832975387573})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.4835807085037231})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.4816884994506836})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.7764413356781006})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6725177764892578})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.7008973360061646})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.708, 'crossentropy': 1.507056640625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3413050174713135})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0614582300186157})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.061868667602539})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0536277294158936})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0087037086486816})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.003735065460205})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 22546], ['id', 12575], ['id', 5893], ['id', 15534], ['id', 50536]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6171100592047447, 1.1388486487078744, 1.5490184316004196, 1.883777156616543, 2.1023227238568847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.4548344612121582})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.117891788482666})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1932885646820068})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2711398601531982})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.3887789249420166})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.4508082866668701})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.535198450088501})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.6242327690124512})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.72, 'crossentropy': 1.33028623046875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2846496105194092})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.068363904953003})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9862579107284546})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9956969022750854})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9731431007385254})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9708470106124878})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 54405], ['id', 54602], ['id', 56245], ['id', 23553], ['id', 32979]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5339500584528558, 0.9509515121305481, 1.332304426826533, 1.6429137885989853, 1.8616114815421607]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.4193124771118164})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1463596820831299})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.060821294784546})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.204357385635376})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3767004013061523})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.3945789337158203})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.71, 'crossentropy': 1.09881181640625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2710318565368652})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0502045154571533})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0265065431594849})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9932920932769775})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9900758266448975})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 22547], ['id', 35305], ['id', 37341], ['id', 21084], ['id', 29088]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.41402132363733846, 0.7790106198043549, 1.1149755510257249, 1.3955124290845466, 1.6488706505414594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.533203125, 'crossentropy': 1.5517516136169434})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.074082851409912})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1032967567443848})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1734955310821533})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.4438308477401733})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.3782367706298828})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.408017873764038})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.4541629552841187})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.6571094989776611})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7803325653076172})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.910111904144287})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7275, 'crossentropy': 1.56436455078125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2851924896240234})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1061211824417114})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0424939393997192})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.030057668685913})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0748155117034912})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0427372455596924})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1546244621276855})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0469090938568115})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.0675246715545654})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.040313959121704})
store['active_learning_steps'][27]['eval_training']['best_epoch']=9
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 13319], ['id', 59858], ['id', 45824], ['id', 165], ['id', 8397]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.486391695526885, 0.9212858270022624, 1.3088635810369458, 1.6272644941309435, 1.8824428937177595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.478515625, 'crossentropy': 1.5459277629852295})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.211242914199829})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.262855052947998})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2702604532241821})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.502970576286316})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.595395565032959})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.783066987991333})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.8846514225006104})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.8767797946929932})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8589651584625244})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6994, 'crossentropy': 1.68744296875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.374431848526001})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1412516832351685})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.094287633895874})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.10697603225708})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1748034954071045})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1005610227584839})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.148301601409912})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.088242769241333})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.129132866859436})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 70], ['id', 35581], ['id', 2122], ['id', 53668], ['id', 52142]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6090593918852478, 1.1106044783039453, 1.5213597845709765, 1.8680558534581646, 2.103575965893633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.509765625, 'crossentropy': 1.4611104726791382})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2436602115631104})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2026877403259277})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.273006796836853})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.4733976125717163})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4334856271743774})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.703, 'crossentropy': 1.179362890625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.4346215724945068})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1366379261016846})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0454668998718262})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0677340030670166})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0300568342208862})
store['active_learning_steps'][29]['eval_training']['best_epoch']=4
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20638], ['id', 42682], ['id', 47079], ['id', 33377], ['id', 14986]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45411971453934896, 0.8785806219404253, 1.2426392289943582, 1.5371316098359298, 1.7748522599445113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.3796675205230713})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1411569118499756})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1769790649414062})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2593562602996826})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3022174835205078})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.4497969150543213})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5897034406661987})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.521733283996582})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.6224451065063477})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.779242753982544})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.830794334411621})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7184, 'crossentropy': 1.54461181640625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3087266683578491})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.070777416229248})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1195647716522217})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0271074771881104})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.01345694065094})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0071046352386475})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0454564094543457})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0496150255203247})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 26462], ['id', 12843], ['id', 52070], ['id', 57208], ['id', 9569]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5422732512267348, 1.0320996956697424, 1.472622745874804, 1.8356366595997553, 2.082411926667416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5029296875, 'crossentropy': 1.4932732582092285})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2285902500152588})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1389834880828857})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1885759830474854})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3846808671951294})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.3213233947753906})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.6575220823287964})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5360358953475952})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6148736476898193})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7244, 'crossentropy': 1.38384755859375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3074166774749756})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1160359382629395})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0488351583480835})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9859381318092346})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.00033438205719})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9849206209182739})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9821166396141052})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9894427061080933})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 19138], ['id', 52675], ['id', 16858], ['id', 2731], ['id', 55866]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5881662020762162, 1.0925410566369598, 1.513616713130368, 1.8550450472425881, 2.0863587043869902]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.4142260551452637})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0901882648468018})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1049165725708008})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1801730394363403})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.2491536140441895})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.304690957069397})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.4319508075714111})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.4243077039718628})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.5759966373443604})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.66975998878479})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.701993465423584})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7279, 'crossentropy': 1.45732431640625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.324303388595581})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.048679232597351})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.982966423034668})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0229904651641846})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.035839557647705})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9975535869598389})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9622598886489868})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.038945198059082})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0150383710861206})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.0095773935317993})
store['active_learning_steps'][32]['eval_training']['best_epoch']=10
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 35107], ['id', 42917], ['id', 42403], ['id', 34739], ['id', 21810]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5282126314836169, 1.017210616141564, 1.458174725848926, 1.8112121323554229, 2.0873794121702423]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.4892578125, 'crossentropy': 1.484635829925537})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1390602588653564})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0914299488067627})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1805375814437866})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.1560537815093994})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.266097903251648})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.313936471939087})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.3888161182403564})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.5312626361846924})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.5219128131866455})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.7413073778152466})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.5957412719726562})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7286, 'crossentropy': 1.58412216796875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.3500562906265259})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0671933889389038})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0161986351013184})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0887211561203003})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0358192920684814})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0438122749328613})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.0220656394958496})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0262577533721924})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9910269975662231})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.0020835399627686})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9980570673942566})
store['active_learning_steps'][33]['eval_training']['best_epoch']=10
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 46632], ['id', 48772], ['id', 40160], ['id', 27747], ['id', 51516]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5537003282919198, 1.0608467469422238, 1.5178725529154278, 1.8862868812968934, 2.1627251386532027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3482282161712646})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0671346187591553})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0858409404754639})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.1493809223175049})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.328021764755249})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.3982582092285156})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.371072769165039})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.509021520614624})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.638747215270996})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.6367379426956177})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.665344476699829})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.8638193607330322})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.837724208831787})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.9085001945495605})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.9170241355895996})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.8165053129196167})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.7972655296325684})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.005936861038208})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.043633460998535})
store['active_learning_steps'][34]['training']['best_epoch']=16
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.73, 'crossentropy': 1.9534876953125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.4903221130371094})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1358156204223633})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.078075885772705})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.075930118560791})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1474008560180664})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1710017919540405})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.140415072441101})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.1387386322021484})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.2047207355499268})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.170682430267334})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.1520968675613403})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1158170700073242})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.166219711303711})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.1772770881652832})
store['active_learning_steps'][34]['eval_training']['best_epoch']=11
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 58065], ['id', 41350], ['id', 18638], ['id', 50700], ['id', 20636]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5949245836706218, 1.135630889173159, 1.6042528477169546, 1.9479336717519757, 2.2131136680054624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.51171875, 'crossentropy': 1.4657396078109741})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.149742603302002})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1373010873794556})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1959986686706543})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3011170625686646})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.3121109008789062})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.350842833518982})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5839130878448486})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.6522797346115112})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.7744650840759277})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7231, 'crossentropy': 1.42231279296875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.332863211631775})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1100739240646362})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.979741096496582})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9816327095031738})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0334362983703613})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9796093702316284})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9663680195808411})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9679388999938965})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9783291816711426})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 18255], ['id', 10674], ['id', 51096], ['id', 17383], ['id', 38890]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5048510422767836, 0.964834932202637, 1.3760153302417049, 1.7400060061960199, 2.0233665655262243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.46484375, 'crossentropy': 1.5042016506195068})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2314975261688232})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0301445722579956})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1070818901062012})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.211256504058838})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2823927402496338})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.383439064025879})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.4135606288909912})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5836682319641113})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6414620876312256})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7121, 'crossentropy': 1.3436138671875}
