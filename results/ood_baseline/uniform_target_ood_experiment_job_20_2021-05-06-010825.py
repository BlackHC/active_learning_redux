store = {}
store['timestamp']=1620259705
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=20']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=20
store['worker_id']=20
store['num_workers']=40
store['config']={'seed': 20, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.356658458709717})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.65586519241333})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6641464233398438})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.126467704772949})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6829, 'crossentropy': 2.0237904296875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 39650], ['ood', 24128], ['id', 26990], ['ood', 58868], ['ood', 57590]], 'labels': [6, 8, 0, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.7934727668762207})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.9570598602294922})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.324787139892578})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.2809460163116455})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6582, 'crossentropy': 1.63423125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 47551], ['ood', 27261], ['ood', 31270], ['id', 40285], ['ood', 47201]], 'labels': [1, 2, 9, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.355830192565918})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7032455205917358})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.0080130100250244})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.797095775604248})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.732, 'crossentropy': 1.20507275390625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 59934], ['id', 5417], ['ood', 30425], ['id', 30697], ['ood', 12453]], 'labels': [0, 5, 1, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.360318660736084})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5339634418487549})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.5920121669769287})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.784470558166504})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7532, 'crossentropy': 1.1334197265625}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 43065], ['id', 37073], ['ood', 3682], ['ood', 27929], ['ood', 39312]], 'labels': [1, 7, 5, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.26034677028656})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.4019702672958374})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.5885709524154663})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.739954948425293})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7285, 'crossentropy': 1.1538755859375}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 29902], ['id', 7350], ['id', 14822], ['id', 40119], ['ood', 58323]], 'labels': [8, 4, 9, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.270611047744751})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3873424530029297})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.5646326541900635})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.7549577951431274})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7398, 'crossentropy': 1.1347412109375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 13783], ['id', 21211], ['ood', 34911], ['ood', 58902], ['ood', 25750]], 'labels': [5, 8, 9, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.1725146770477295})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.2700153589248657})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.2993810176849365})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.4831821918487549})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7728, 'crossentropy': 0.97830029296875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 15733], ['ood', 43734], ['id', 47546], ['id', 9529], ['ood', 38464]], 'labels': [6, 2, 8, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.1323105096817017})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.1795202493667603})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.3220241069793701})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.5047101974487305})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7867, 'crossentropy': 1.007278515625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 6914], ['ood', 25078], ['id', 7583], ['id', 58218], ['ood', 31734]], 'labels': [7, 4, 5, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.123667597770691})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1537864208221436})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.2355619668960571})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.3684402704238892})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7878, 'crossentropy': 0.96102890625}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 31833], ['ood', 5524], ['id', 5170], ['id', 57136], ['id', 47098]], 'labels': [7, 6, 8, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.030637502670288})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0853185653686523})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2193577289581299})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2072796821594238})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7857, 'crossentropy': 0.97827822265625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 32204], ['ood', 30901], ['ood', 17438], ['ood', 26724], ['id', 28920]], 'labels': [2, 3, 9, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.06459379196167})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1267648935317993})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.083812952041626})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.2747924327850342})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7916, 'crossentropy': 0.96086552734375}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 3460], ['id', 26169], ['id', 45969], ['id', 32905], ['id', 33433]], 'labels': [9, 7, 9, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9783952236175537})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0106115341186523})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.104528546333313})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1163150072097778})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.793, 'crossentropy': 0.94126826171875}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 40039], ['id', 40936], ['ood', 49557], ['id', 25621], ['id', 26989]], 'labels': [5, 2, 7, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9571800231933594})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.881111204624176})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0188332796096802})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.116056203842163})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.119338870048523})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8329, 'crossentropy': 0.786782177734375}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 36124], ['id', 49327], ['ood', 52555], ['ood', 28607], ['ood', 58840]], 'labels': [4, 7, 5, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.935608983039856})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9367774724960327})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0421253442764282})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1136932373046875})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8168, 'crossentropy': 0.86080078125}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 2176], ['id', 13456], ['ood', 36588], ['id', 44544], ['ood', 7954]], 'labels': [1, 9, 1, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.960442304611206})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8876597881317139})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9693315029144287})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9592076539993286})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9982333183288574})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8357, 'crossentropy': 0.779702978515625}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 27976], ['id', 13170], ['id', 1518], ['id', 19208], ['ood', 12263]], 'labels': [0, 6, 9, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9200081825256348})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8799440860748291})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9228344559669495})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9777628183364868})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.041599988937378})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8405, 'crossentropy': 0.7990201171875}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 15305], ['ood', 27914], ['ood', 41548], ['id', 26779], ['id', 36707]], 'labels': [0, 5, 1, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9080541133880615})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9303123354911804})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0433032512664795})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.021983027458191})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8206, 'crossentropy': 0.84558974609375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 6704], ['ood', 24012], ['ood', 54280], ['id', 36829], ['id', 33768]], 'labels': [0, 2, 5, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9049637317657471})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9090299606323242})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.899943470954895})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.987602949142456})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0275092124938965})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0482547283172607})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.845, 'crossentropy': 0.817629638671875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 39157], ['ood', 3284], ['ood', 17937], ['id', 58618], ['ood', 38993]], 'labels': [1, 1, 2, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9440498352050781})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9290398955345154})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9756932258605957})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0868546962738037})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0586012601852417})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8258, 'crossentropy': 0.83088359375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 35353], ['id', 31993], ['ood', 1704], ['id', 41446], ['id', 50901]], 'labels': [8, 1, 3, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9528728723526001})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8854515552520752})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8904296159744263})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.92305988073349})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0044502019882202})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8369, 'crossentropy': 0.817001318359375}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 23971], ['ood', 39478], ['id', 43356], ['id', 41408], ['ood', 59167]], 'labels': [7, 3, 7, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8546292781829834})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8757168054580688})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.844283938407898})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0234140157699585})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9236835241317749})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9868136644363403})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8444, 'crossentropy': 0.790333251953125}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 41554], ['id', 10043], ['id', 22427], ['id', 51840], ['ood', 29174]], 'labels': [8, 9, 1, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9612432718276978})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9544864892959595})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9510160684585571})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9523779153823853})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9714717268943787})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1063909530639648})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8239, 'crossentropy': 0.91178779296875}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 24884], ['id', 41592], ['id', 47968], ['ood', 26281], ['ood', 4361]], 'labels': [7, 8, 5, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9385104179382324})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8186980485916138})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9351259469985962})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9568454623222351})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.010124921798706})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8422, 'crossentropy': 0.766834033203125}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 28981], ['ood', 44544], ['ood', 56311], ['id', 33862], ['ood', 12232]], 'labels': [5, 3, 0, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0060703754425049})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8920601606369019})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9185242652893066})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9868174195289612})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.032931923866272})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8422, 'crossentropy': 0.7951671875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 14433], ['id', 21261], ['id', 45163], ['ood', 29540], ['id', 45659]], 'labels': [4, 3, 9, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8921329975128174})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8024383187294006})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8555428981781006})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9155557751655579})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8543256521224976})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8552, 'crossentropy': 0.728855712890625}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 1700], ['ood', 37248], ['ood', 34708], ['id', 50785], ['id', 12523]], 'labels': [9, 2, 5, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9475423097610474})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9584344029426575})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0133202075958252})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2441716194152832})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8137, 'crossentropy': 0.8605134765625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 46391], ['ood', 18653], ['id', 3158], ['id', 14065], ['ood', 6527]], 'labels': [0, 5, 8, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9273760318756104})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8976907730102539})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9178725481033325})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.891044020652771})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.978669285774231})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0425307750701904})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9851415157318115})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8474, 'crossentropy': 0.8224552734375}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 55778], ['id', 15771], ['ood', 53924], ['id', 51426], ['id', 54940]], 'labels': [8, 5, 6, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8736139535903931})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8608435392379761})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7919973134994507})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9449147582054138})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9442980885505676})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9807723164558411})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8607, 'crossentropy': 0.756650927734375}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 59585], ['id', 42315], ['ood', 44875], ['id', 40297], ['id', 21242]], 'labels': [4, 9, 5, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9525853991508484})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9422413110733032})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0434247255325317})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0762040615081787})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1612297296524048})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.832, 'crossentropy': 0.85967236328125}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 42191], ['id', 10484], ['ood', 18496], ['ood', 9930], ['id', 40280]], 'labels': [2, 6, 8, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.865662693977356})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.789476752281189})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7705156207084656})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8358595371246338})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8396649360656738})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.874531626701355})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.695727734375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 14238], ['ood', 43728], ['ood', 6976], ['id', 16314], ['ood', 50906]], 'labels': [7, 7, 2, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9357656240463257})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8753988742828369})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8436763286590576})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9759358167648315})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9526998996734619})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.07373046875})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8509, 'crossentropy': 0.784981591796875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 25216], ['ood', 261], ['id', 25014], ['id', 9934], ['id', 35448]], 'labels': [9, 3, 4, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9232532978057861})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.847022294998169})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8446937799453735})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9126861691474915})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8913366794586182})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9478822946548462})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8628, 'crossentropy': 0.738633837890625}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 31799], ['ood', 18894], ['ood', 15969], ['ood', 13808], ['id', 31287]], 'labels': [5, 5, 8, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0032553672790527})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.873697817325592})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8324059247970581})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.841856837272644})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9283266067504883})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0221401453018188})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8525, 'crossentropy': 0.7407185546875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 41988], ['ood', 26983], ['ood', 58647], ['ood', 36189], ['id', 20219]], 'labels': [6, 4, 4, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.9283725023269653})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8233519792556763})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8661894798278809})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9867514371871948})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9103035926818848})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.858, 'crossentropy': 0.704181640625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 41346], ['ood', 38492], ['ood', 14601], ['id', 23020], ['ood', 56597]], 'labels': [6, 5, 1, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.0337976217269897})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8738888502120972})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8155844211578369})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8318676948547363})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8655409812927246})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0226452350616455})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8703, 'crossentropy': 0.683887548828125}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 47418], ['ood', 10649], ['ood', 53443], ['ood', 18922], ['id', 53880]], 'labels': [7, 8, 6, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9533026218414307})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8622488975524902})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8304449319839478})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9134379625320435})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9362192153930664})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9590065479278564})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8522, 'crossentropy': 0.77717900390625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 46016], ['ood', 40591], ['ood', 1647], ['ood', 28903], ['id', 3956]], 'labels': [7, 6, 0, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0048085451126099})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7782304286956787})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.809572160243988})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8606606125831604})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8437554240226746})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8544, 'crossentropy': 0.721055517578125}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 22364], ['id', 51952], ['id', 49619], ['ood', 53442], ['ood', 37601]], 'labels': [7, 1, 9, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.9612221717834473})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8055322766304016})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7718076705932617})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7991576194763184})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8355951309204102})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8864016532897949})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8651, 'crossentropy': 0.690943212890625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 27370], ['id', 25857], ['id', 47802], ['id', 12958], ['ood', 33019]], 'labels': [9, 1, 3, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.953155517578125})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.812930166721344})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8366855382919312})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9240449666976929})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0640325546264648})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8489, 'crossentropy': 0.72363310546875}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 14706], ['ood', 55203], ['ood', 5147], ['ood', 31464], ['id', 21576]], 'labels': [8, 5, 6, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.912933349609375})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8185871839523315})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8172242641448975})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9343048334121704})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8498131036758423})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8908276557922363})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8661, 'crossentropy': 0.69341953125}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 14236], ['ood', 39803], ['ood', 22638], ['id', 55924], ['id', 22667]], 'labels': [3, 9, 3, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.9898865222930908})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8069077730178833})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8072415590286255})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8325273990631104})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9049423933029175})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8625, 'crossentropy': 0.696078173828125}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 31370], ['ood', 25818], ['ood', 58391], ['ood', 46497], ['ood', 41223]], 'labels': [1, 4, 9, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9558215737342834})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7753555178642273})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8351161479949951})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9033274054527283})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8802182674407959})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8502, 'crossentropy': 0.7124220703125}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 4044], ['ood', 48884], ['ood', 28866], ['ood', 35569], ['ood', 45700]], 'labels': [1, 8, 0, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9785777926445007})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7957571744918823})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7966364026069641})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9309762716293335})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8608185648918152})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8583, 'crossentropy': 0.688265478515625}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 17163], ['ood', 4814], ['ood', 9507], ['ood', 24279], ['id', 36443]], 'labels': [5, 6, 3, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.9760575890541077})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8475686311721802})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8502651453018188})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8660005927085876})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8930789828300476})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8491, 'crossentropy': 0.735855029296875}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 9], ['ood', 8456], ['ood', 50376], ['ood', 5229], ['id', 1548]], 'labels': [4, 5, 0, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9578094482421875})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8865915536880493})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8192357420921326})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8604071140289307})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.88036048412323})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8032846450805664})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9669724702835083})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9664781093597412})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9707914590835571})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8833, 'crossentropy': 0.69217607421875}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 13017], ['ood', 3395], ['ood', 57208], ['id', 16068], ['ood', 46074]], 'labels': [3, 4, 0, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9079854488372803})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7292664051055908})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7681001424789429})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7548431158065796})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8099797964096069})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8624, 'crossentropy': 0.6535138671875}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 31720], ['id', 3585], ['ood', 12137], ['ood', 35678], ['ood', 30555]], 'labels': [3, 0, 2, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9284096956253052})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8275514245033264})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8784273862838745})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9357171058654785})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0144156217575073})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8367, 'crossentropy': 0.763056396484375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 19374], ['ood', 12887], ['ood', 55993], ['id', 49446], ['id', 34606]], 'labels': [5, 0, 6, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9878222942352295})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8451676368713379})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7798995971679688})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8723609447479248})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.803623616695404})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7972931265830994})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8653, 'crossentropy': 0.679709423828125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 21048], ['ood', 27818], ['ood', 43638], ['id', 24375], ['ood', 55132]], 'labels': [5, 2, 3, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9876166582107544})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7675000429153442})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8307818174362183})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8830484747886658})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9089276790618896})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8627, 'crossentropy': 0.6837998046875}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 12421], ['id', 39645], ['id', 55828], ['ood', 14607], ['id', 48595]], 'labels': [8, 5, 4, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9384515285491943})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7425674200057983})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7325534224510193})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.797237753868103})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7512891292572021})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7750309705734253})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8845, 'crossentropy': 0.61175927734375}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 18093], ['ood', 3840], ['ood', 1975], ['ood', 29416], ['ood', 49924]], 'labels': [8, 7, 1, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9034085273742676})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7731268405914307})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8442705869674683})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7509263753890991})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8641546964645386})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.869330883026123})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8952707648277283})
store['active_learning_steps'][50]['training']['best_epoch']=4
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.872, 'crossentropy': 0.671901904296875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 51178], ['id', 52725], ['id', 31540], ['ood', 57132], ['ood', 43766]], 'labels': [7, 6, 8, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8534880876541138})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7711877822875977})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7100294828414917})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8325151205062866})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.745990514755249})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8122221231460571})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8825, 'crossentropy': 0.614305908203125}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 24288], ['ood', 971], ['ood', 12309], ['ood', 18348], ['ood', 9669]], 'labels': [3, 9, 5, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.005798101425171})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7792310118675232})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8208431005477905})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8555504083633423})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8864991068840027})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8584, 'crossentropy': 0.713257568359375}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 29015], ['ood', 28280], ['ood', 5201], ['id', 39110], ['ood', 16977]], 'labels': [6, 6, 8, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8814684152603149})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.738660991191864})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7774279117584229})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7997308969497681})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8652501702308655})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.87, 'crossentropy': 0.6511740234375}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 46054], ['ood', 22032], ['id', 17495], ['id', 14562], ['ood', 24718]], 'labels': [0, 9, 5, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9295856952667236})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7621210813522339})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7141635417938232})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.794777512550354})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8428197503089905})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7924659252166748})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8812, 'crossentropy': 0.608278173828125}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 34795], ['ood', 6988], ['ood', 20643], ['id', 19764], ['ood', 38531]], 'labels': [6, 5, 6, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9669297933578491})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7554318904876709})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7343765497207642})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7784148454666138})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7633612155914307})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7717029452323914})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8888, 'crossentropy': 0.594405224609375}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 55435], ['ood', 44293], ['id', 10192], ['id', 38962], ['ood', 56535]], 'labels': [9, 2, 5, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9876924157142639})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7905436754226685})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7120199203491211})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7969337701797485})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8009350299835205})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7546573877334595})
store['active_learning_steps'][56]['training']['best_epoch']=3
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8925, 'crossentropy': 0.5844615234375}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 50150], ['id', 33211], ['ood', 48550], ['id', 2541], ['id', 38126]], 'labels': [8, 9, 0, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8709285259246826})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.693645715713501})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.714858889579773})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7525075674057007})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.749954342842102})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8837, 'crossentropy': 0.611691455078125}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 7900], ['id', 16930], ['ood', 43640], ['id', 31064], ['ood', 35116]], 'labels': [1, 1, 1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9817951917648315})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7547715306282043})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6984225511550903})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7181567549705505})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7224611043930054})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8727318048477173})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8859, 'crossentropy': 0.626419775390625}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 12810], ['id', 267], ['id', 50475], ['ood', 8626], ['ood', 44378]], 'labels': [6, 9, 2, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.9978458881378174})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.681541919708252})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6702544689178467})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7356934547424316})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6847267150878906})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.698485255241394})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8902, 'crossentropy': 0.580382373046875}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 4974], ['id', 7709], ['id', 41298], ['id', 50766], ['id', 28512]], 'labels': [9, 0, 4, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.850740909576416})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6302325129508972})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6669375896453857})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6412068009376526})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6855058670043945})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8915, 'crossentropy': 0.568571142578125}
store['active_learning_steps'][60]['acquisition']={'indices': [['ood', 38184], ['id', 18510], ['ood', 31301], ['id', 4054], ['ood', 16869]], 'labels': [2, 9, 4, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.003798246383667})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6794819831848145})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6405136585235596})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6823136210441589})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6973035335540771})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6888429522514343})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9049, 'crossentropy': 0.513455908203125}
store['active_learning_steps'][61]['acquisition']={'indices': [['ood', 46856], ['ood', 48446], ['id', 1569], ['ood', 31207], ['ood', 54478]], 'labels': [5, 2, 9, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9633466005325317})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6652439832687378})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6901659965515137})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6949864625930786})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6446024179458618})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7251397967338562})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9071735143661499})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8304628133773804})
store['active_learning_steps'][62]['training']['best_epoch']=5
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.520698046875}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 10867], ['ood', 51704], ['id', 55443], ['id', 41962], ['ood', 29533]], 'labels': [9, 2, 2, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.865759551525116})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6690109968185425})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6429084539413452})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6697385311126709})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7300050854682922})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6599307060241699})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8886, 'crossentropy': 0.563850537109375}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 56849], ['id', 39309], ['ood', 48434], ['id', 6579], ['id', 40255]], 'labels': [8, 0, 1, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9431929588317871})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6985354423522949})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6727595925331116})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7389519810676575})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6847419738769531})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7635948061943054})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8951, 'crossentropy': 0.565651513671875}
store['active_learning_steps'][64]['acquisition']={'indices': [['ood', 47926], ['ood', 8968], ['ood', 1463], ['id', 26922], ['ood', 28]], 'labels': [0, 7, 1, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.827431857585907})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6277607679367065})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6760982871055603})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6946581602096558})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5850695371627808})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7204642295837402})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6745207905769348})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7986736297607422})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.5009849609375}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 49104], ['ood', 15376], ['id', 45019], ['ood', 28650], ['ood', 52233]], 'labels': [6, 4, 8, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9051738977432251})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6495339274406433})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6467949151992798})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6731672883033752})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7025630474090576})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.629852294921875})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6821960210800171})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6792900562286377})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7049956321716309})
store['active_learning_steps'][66]['training']['best_epoch']=6
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.510705078125}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 46006], ['ood', 56123], ['id', 34292], ['id', 49139], ['ood', 35933]], 'labels': [6, 6, 9, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8462510704994202})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6581578254699707})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6268308758735657})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6530168652534485})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6079953908920288})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6388776302337646})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6683031320571899})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6621087789535522})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9069, 'crossentropy': 0.52895869140625}
store['active_learning_steps'][67]['acquisition']={'indices': [['ood', 49098], ['id', 47496], ['id', 14214], ['ood', 50034], ['id', 29627]], 'labels': [1, 3, 5, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.904000997543335})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6300362944602966})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6349512338638306})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6508592963218689})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6779081225395203})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.55627939453125}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 19784], ['ood', 10643], ['id', 22146], ['ood', 40356], ['id', 10026]], 'labels': [2, 5, 2, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8735587000846863})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6237993240356445})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6289916038513184})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6243545413017273})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6711836457252502})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8992, 'crossentropy': 0.542205029296875}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 58278], ['ood', 30987], ['ood', 38711], ['id', 7328], ['id', 51099]], 'labels': [9, 2, 5, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8958107233047485})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6886143684387207})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6558027863502502})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7060590982437134})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6850213408470154})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6920279264450073})
store['active_learning_steps'][70]['training']['best_epoch']=3
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8935, 'crossentropy': 0.56281640625}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 26496], ['ood', 18525], ['ood', 31561], ['id', 56397], ['ood', 56604]], 'labels': [8, 3, 9, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9649985432624817})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6630155444145203})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6876122355461121})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6446313261985779})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.621108889579773})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6550697088241577})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6860001087188721})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7343397736549377})
store['active_learning_steps'][71]['training']['best_epoch']=5
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.49806103515625}
store['active_learning_steps'][71]['acquisition']={'indices': [['ood', 3789], ['id', 52298], ['id', 40770], ['id', 14713], ['id', 2143]], 'labels': [1, 3, 1, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8888769149780273})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6632610559463501})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6215547323226929})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6303415894508362})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6686991453170776})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6530669927597046})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9065, 'crossentropy': 0.508840185546875}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 20996], ['ood', 36032], ['id', 1667], ['id', 11379], ['id', 51074]], 'labels': [7, 7, 4, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8979905843734741})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6469128131866455})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6393970251083374})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6656911373138428})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.615262508392334})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6938868165016174})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7288049459457397})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6690414547920227})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.51640478515625}
store['active_learning_steps'][73]['acquisition']={'indices': [['ood', 50874], ['ood', 31926], ['ood', 8350], ['ood', 38889], ['id', 31160]], 'labels': [5, 7, 9, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8353433609008789})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6896267533302307})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6375390291213989})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7310293912887573})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6809382438659668})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.686087965965271})
store['active_learning_steps'][74]['training']['best_epoch']=3
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.537851611328125}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 17763], ['id', 50988], ['ood', 59044], ['id', 9292], ['id', 59613]], 'labels': [3, 8, 4, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8486354947090149})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6823853254318237})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6465601921081543})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5851269960403442})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5981164574623108})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.718407392501831})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.705991804599762})
store['active_learning_steps'][75]['training']['best_epoch']=4
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.50090205078125}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 18649], ['id', 37829], ['id', 6450], ['id', 56716], ['id', 16535]], 'labels': [1, 6, 3, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8445482850074768})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6234028935432434})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5456152558326721})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6932927370071411})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5860801935195923})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5919278860092163})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.4555689453125}
store['active_learning_steps'][76]['acquisition']={'indices': [['ood', 10925], ['ood', 1391], ['id', 59884], ['id', 33053], ['id', 15008]], 'labels': [7, 6, 8, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8953918814659119})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6385416984558105})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6031168699264526})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5803530216217041})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7100517153739929})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.653188943862915})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6804685592651367})
store['active_learning_steps'][77]['training']['best_epoch']=4
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9137, 'crossentropy': 0.494298046875}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 19398], ['id', 4933], ['id', 24131], ['id', 57871], ['ood', 57750]], 'labels': [5, 1, 7, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9232840538024902})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.605130136013031})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6269292831420898})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6404318809509277})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6533257961273193})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8957, 'crossentropy': 0.557199755859375}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 38766], ['id', 6255], ['ood', 25811], ['ood', 42711], ['id', 41731]], 'labels': [0, 5, 2, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9947436451911926})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6525726318359375})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6153337955474854})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6454793214797974})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6224969625473022})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6331878304481506})
store['active_learning_steps'][79]['training']['best_epoch']=3
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.504762646484375}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 8110], ['ood', 52200], ['id', 12648], ['id', 38475], ['id', 50669]], 'labels': [0, 3, 8, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8235787153244019})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6387845277786255})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6356779336929321})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.665881872177124})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7030871510505676})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6782861948013306})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.516144482421875}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 10088], ['ood', 45240], ['id', 16045], ['id', 17715], ['ood', 41777]], 'labels': [7, 5, 0, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9410548806190491})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6328499913215637})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6579005718231201})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6394401788711548})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6163158416748047})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6623857021331787})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6116509437561035})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6858829855918884})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6229865550994873})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7344774603843689})
store['active_learning_steps'][81]['training']['best_epoch']=7
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.510389501953125}
store['active_learning_steps'][81]['acquisition']={'indices': [['ood', 43022], ['id', 7850], ['ood', 12903], ['ood', 6838], ['id', 37088]], 'labels': [6, 1, 3, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8060044050216675})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6405732035636902})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5912207365036011})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5726372003555298})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5505262613296509})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5748878717422485})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5844522714614868})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5794510245323181})
store['active_learning_steps'][82]['training']['best_epoch']=5
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9176, 'crossentropy': 0.47442548828125}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 8150], ['id', 17072], ['ood', 49898], ['id', 19742], ['ood', 26933]], 'labels': [6, 1, 8, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8605492115020752})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6833040118217468})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6457763314247131})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5742308497428894})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6282564401626587})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6547523736953735})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7524769306182861})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9131, 'crossentropy': 0.4766865234375}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 30275], ['ood', 48532], ['ood', 48115], ['ood', 57585], ['id', 58851]], 'labels': [0, 5, 6, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8952223062515259})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6441538333892822})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5593658685684204})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6026678681373596})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6120568513870239})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6305249929428101})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9096, 'crossentropy': 0.507116015625}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 17259], ['ood', 49162], ['id', 45127], ['id', 57902], ['id', 42295]], 'labels': [0, 0, 6, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9134286046028137})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.590244710445404})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5901719927787781})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5730836391448975})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5834959149360657})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.619904637336731})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6380692720413208})
store['active_learning_steps'][85]['training']['best_epoch']=4
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.485030908203125}
store['active_learning_steps'][85]['acquisition']={'indices': [['ood', 40796], ['ood', 23892], ['ood', 21871], ['ood', 55818], ['id', 1512]], 'labels': [2, 7, 3, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8406674861907959})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6357576847076416})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6719095706939697})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5891109108924866})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6368963718414307})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6276681423187256})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6235337257385254})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.51440673828125}
